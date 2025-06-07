from django.shortcuts import render


def handler404(request, exception, template_name="errors/404.html"):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def page_under_construction(request):
    """ Placeholder for subpage not yet available"""
    return render(request, 'errors/page_under_construction.html')
