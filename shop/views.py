from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from django.db.models import Q
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import ImageTheme, Product, PolicyPage

import logging

logger = logging.getLogger(__name__)


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


class PolicyPageView(TemplateView):
    """
    Display a single policy document
    from :model:`shop.PolicyPage` based on the URL slug.

    **Context:**

    ``policy``
        An instance of :model:`shop.PolicyPage` matching the given slug.

    **Template:**

    :template:`shop/policy_page.html`
    """
    template_name = 'shop/policy_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')  # e.g., 'privacy'
        context['policy'] = PolicyPage.objects.get(title=slug)
        return context


class ContactPage(FormView):
    """
    Display the contact form page and handle contact form submissions.

    Submissions are processed via POST
    and validated using :form:`shop.ContactForm`.
    Upon valid submission,
    an email is sent to the administrator with the message details.

    **Form:**

    :form:`shop.ContactForm`

    **Context:**

    ``form``
        The contact form instance.

    **Template:**

    :template:`shop/contact_form.html`
    """
    template_name = 'shop/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_page')

    def form_valid(self, form):
        """
        Process a valid form submission.

        Sends an email to the site administrator containing the sender's name,
        email, and message.

        :param form: Validated instance of :form:`shop.ContactForm`.
        :return: Redirect to the success URL.
        """
        try:
            send_mail(
                subject=f"Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['annisch78@gmail.com'],
                fail_silently=False,
            )
            messages.success(
                self.request,
                "Your message has been sent successfully."
            )
        except (BadHeaderError, SMTPException, Exception) as e:
            logger.error("Contact form failed to send: %s", e)
            messages.error(
                self.request,
                "There was an error sending your message."
                "Please try again later."
            )
        return super().form_valid(form)
