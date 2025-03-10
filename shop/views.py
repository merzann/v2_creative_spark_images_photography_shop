from django.shortcuts import render


def index(request):
    """
    Displays the shop homepage.
    """
    return render(request, "shop/index.html")
