from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModuleForm
# BASE VIEW CLASS = View


class CourseObjectMixin(object):
    model = Course

    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class CourseCreateView(View):
    template_name = "courses/course_create.html"  # DetailView
    # GET method

    def get(self, request, *args, **kwargs):
        print("*** App: courses - views.py CourseCreateView:get ")
        form = CourseModuleForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print("*** App: courses - views.py CourseCreateView:post ")
        form = CourseModuleForm(request.POST)
        if form.is_valid():
            print("   *** Saving form")
            form.save()
            print("   *** Reinitialize empty form")
            form = CourseModuleForm()
        context = {"form": form}
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_update.html"

    def get(self, request, id=None, *args, **kwargs):
        print("*** App: courses - views.py CourseUpdateView:get ")
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModuleForm(instance=obj)
            context["object"] = obj
            context["form"] = form
        return render(request, self.template_name, context)


class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html"

    def get(self, request, id=None, *args, **kwargs):
        print("*** App: courses - views.py CourseDeleteView:get ")
        context = {}
        obj = self.get_object()
        if obj is not None:
            context["object"] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        print("*** App: courses - views.py CourseUpdateView:post ")
        context = {}
        obj = self.get_object()
        if obj is not None:
            print("   *** Deleting form")
            obj.delete()
            context["object"] = None
            return redirect("/courses/")
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "courses/course_list.html"  # DetailView
    queryset = Course.objects.all()

    def get_queryset(self):
        print("*** App: Courses - CourseListView => queryset")
        print(self.queryset)
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {"object_list": self.get_queryset()}
        return render(request, self.template_name, context)


# class MyListView(CourseListView):
#     queryset = Course.objects.filter(id=1)


class CourseView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html"  # DetailView
    # GET method

    def get(self, request, id=None, *args, **kwargs):
        context = {"object": self.get_object()}
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     return render(request, "about.html", {})


# Create your views here.
# HTPP METHODS


def my_fbv(request, *args, **kwargs):
    return render(request, "about.html", {})
