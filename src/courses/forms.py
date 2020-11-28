from django import forms
from .models import Course


class CourseModuleForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "title"
        ]
