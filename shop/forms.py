from django import forms
from products.models import Product


class ContactForm(forms.Form):
    """
    A contact form for customers to send inquiries or messages.
    All fields are required. The message field is limited to 1000 characters.

    **Template:**

    :template:`shop/contact_form.html`
    """
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_name',
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'id_email',
        })
    )
    message = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'id_message',
        }),
        help_text="Max 1000 characters.",
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "theme",
            "tags",
            "product_types",
            "price",
            "license_types",
            "print_types",
            "size",
            "stock",
            "image_preview",
            "image_framed",
            "image_canvas",
            "image_room_mockup",
            "file",
        ]
