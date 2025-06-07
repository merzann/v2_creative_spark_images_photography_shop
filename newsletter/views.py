from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import NewsletterForm


@require_POST
def newsletter_signup(request):
    """
    Handle AJAX-based newsletter signup form submission.

    Validates and saves the submitted email address using
    :form:`newsletter.NewsletterForm`.

    **Returns:**
        JsonResponse: Success status or error details if form is invalid.
    """
    form = NewsletterForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)
