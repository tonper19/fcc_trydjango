from django import forms
from .models import Friend


class FriendModelForm(forms.ModelForm):

    class Meta:
        model = Friend
        fields = [
            'name',
            'lives_in',
            'email',
        ]
