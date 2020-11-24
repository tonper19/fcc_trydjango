from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
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
                "rows": 20,
                "cols": 60
            }
        )
    )
    active = forms.BooleanField(initial=True)

    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'active',
        ]
