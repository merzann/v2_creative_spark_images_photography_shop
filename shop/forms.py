from django import forms


class ContactForm(forms.Form):
    """
    A contact form for customers to send inquiries or messages.
    All fields are required. The message field is limited to 1000 characters.

    **Template:**

    :template:`shop/contact_form.html`
    """
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 1000}),
        max_length=1000,
        required=True,
        help_text="Max 1000 characters.",
    )
