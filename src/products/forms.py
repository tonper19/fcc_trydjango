from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
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

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "TA" in title:
            raise forms.ValidationError("Title must contain the word TA")
        return title

    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if not 1 <= price <= 10000:
            raise forms.ValidationError("price must be between 1 and 10000")
        return price


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
