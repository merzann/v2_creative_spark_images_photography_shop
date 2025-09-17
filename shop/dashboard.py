from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate, TruncMonth, TruncYear
from django.urls import reverse

from .models import OrderModel, Product
from shop.forms import ProductForm

import json


@staff_member_required
def sales_dashboard(request):
    # KPIs
    total_sales = OrderModel.objects.count()
    agg = OrderModel.objects.aggregate(total=Sum("total_price"))
    total_revenue = agg["total"] or 0
    top_product = (
        Product.objects.annotate(order_count=Count('orders'))
        .order_by('-order_count')
        .first()
    )
    top_product_name = top_product.title if top_product else "N/A"

    # --- Sales by Day ---
    sales_by_day = (
        OrderModel.objects
        .annotate(day=TruncDate('created_at'))
        .values('day')
        .annotate(total=Sum('total_price'))
        .order_by('day')
    )
    labels_day = [entry['day'].strftime('%d %b') for entry in sales_by_day]
    data_day = [float(entry['total']) for entry in sales_by_day]

    # --- Sales by Month ---
    sales_by_month = (
        OrderModel.objects
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Sum('total_price'))
        .order_by('month')
    )
    labels_month = [
        entry["month"].strftime("%b %Y")
        for entry in sales_by_month
    ]
    data_month = [float(entry['total']) for entry in sales_by_month]

    # --- Sales by Year ---
    sales_by_year = (
        OrderModel.objects
        .annotate(year=TruncYear('created_at'))
        .values('year')
        .annotate(total=Sum('total_price'))
        .order_by('year')
    )
    labels_year = [entry['year'].strftime('%Y') for entry in sales_by_year]
    data_year = [float(entry['total']) for entry in sales_by_year]

    return render(request, "shop/sales_dashboard.html", {
        "total_sales": total_sales,
        "total_revenue": total_revenue,
        "top_product": top_product_name,

        # Daily
        "labels_daily": json.dumps(labels_day),
        "data_daily": json.dumps(data_day),

        # Monthly
        "labels_monthly": json.dumps(labels_month),
        "data_monthly": json.dumps(data_month),

        # Yearly
        "labels_yearly": json.dumps(labels_year),
        "data_yearly": json.dumps(data_year),
    })


def staff_dashboard(request):
    form = ProductForm()

    if request.method == "POST":
        action = request.POST.get("action", "").strip()

        # --- Add Product ---
        if action == "add_product":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "New product added successfully.")
                return redirect(reverse("staff_dashboard") + "#add-product")

        elif action == "edit_order":
            order_id = request.POST.get("order_id")
            new_status = request.POST.get("status", "").strip().lower()
            allowed = {"pending", "processing", "completed", "cancelled"}
            order = get_object_or_404(OrderModel, pk=order_id)

            if new_status in allowed:
                order.status = new_status
                order.save()
                messages.success(
                    request, f"Order #{order.id} updated to '{new_status}'."
                )
            else:
                messages.error(request, "Invalid status value.")

            return redirect(reverse("staff_dashboard") + "#manage-orders")

        elif action == "delete_order":
            order_id = request.POST.get("order_id")
            order = get_object_or_404(OrderModel, pk=order_id)
            order.delete()
            messages.success(request, f"Order #{order_id} deleted.")

            return redirect(reverse("staff_dashboard") + "#manage-orders")

        else:
            messages.error(request, "Unknown action.")

    orders = OrderModel.objects.all().order_by("-created_at")

    return render(
        request,
        "shop/staff_dashboard.html",
        {"form": form, "orders": orders},
    )
