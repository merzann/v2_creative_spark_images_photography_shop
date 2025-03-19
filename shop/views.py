from django.shortcuts import render, get_object_or_404
from .models import ImageTheme, Product


def shop_page(request):
    """
    Display all :model:`shop.ImageTheme` instances in the gallery.

    **Context:**

    ``themes``
        A queryset containing all instances of :model:`shop.ImageTheme`.

    **Template:**

    :template:`shop/shop.html`
    """
    themes = ImageTheme.objects.all()
    return render(request, "shop/shop.html", {"themes": themes})


def images_by_theme(request, theme_slug):
    """
    Display all :model:`shop.Product` instances related to a specific
    :model:`shop.ImageTheme`.

    **Context:**

    ``theme``
        An instance of :model:`shop.ImageTheme` matching the given slug.
    ``images``
        A queryset containing all instances of :model:`shop.Product`
        associated with the given theme.

    **Template:**

    :template:`shop/images_by_theme.html`
    """
    theme = get_object_or_404(ImageTheme, slug=theme_slug)
    images = Product.objects.filter(theme=theme)
    return render(
        request,
        "shop/images_by_theme.html",
        {"theme": theme, "images": images},
    )
