from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import ImageTheme, Product


def gallery_page(request):
    """
    Display all :model:`shop.ImageTheme` instances in the gallery,
    with optional search functionality.

    If a search query is provided via the `q` GET parameter, the queryset
    is filtered to include only themes whose title or description contains
    the search term (case-insensitive).

    **Context:**

    ``themes``
        A queryset of filtered or all instances of :model:`shop.ImageTheme`.

    ``search_term``
        The current search query string, if any.

    **Template:**

    :template:`shop/gallery_page.html`
    """
    query = request.GET.get("q", "")
    themes = ImageTheme.objects.all()

    if query:
        themes = themes.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    context = {
        "themes": themes,
        "search_term": query,
    }
    return render(request, "shop/gallery_page.html", context)


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
