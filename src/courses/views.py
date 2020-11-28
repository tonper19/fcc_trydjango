from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course
# BASE VIEW CLASS = View


class CourseView(View):
    template_name = "courses/course_detail.html"  # DetailView
    # GET method

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context["object"] = obj
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     return render(request, "about.html", {})


# Create your views here.
# HTPP METHODS


def my_fbv(request, *args, **kwargs):
    return render(request, "about.html", {})
