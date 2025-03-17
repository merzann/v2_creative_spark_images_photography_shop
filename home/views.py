from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def shop(request):
    return render(request, "shops.html")
