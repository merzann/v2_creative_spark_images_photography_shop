from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product
from shop.models import ImageTheme
from home.models import AboutUs


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "gallery_page",
            "newsletter_page",
            "about",
            "contact_page",
        ]

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.all()


class ThemeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return ImageTheme.objects.all()


class AboutUsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4

    def items(self):
        return AboutUs.objects.all()
