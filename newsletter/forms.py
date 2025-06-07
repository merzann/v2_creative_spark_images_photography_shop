from django import forms
from .models import NewsletterSignup


class NewsletterForm(forms.ModelForm):
    """
    Form for collecting user email addresses for the newsletter signup.

    **Model:**
    :model:`newsletter.NewsletterSignup`
    """
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = NewsletterSignup
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email...',
                'class': 'form-control'
            }),
        }
