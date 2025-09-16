from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import OrderModel, Product
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate, TruncMonth, TruncYear

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
