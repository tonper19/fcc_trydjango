from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the title"
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter the description",
                "class": "html-new-class-name html-another-class",
                "id": "html-id",
                "rows": 3,
                "cols": 10
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
