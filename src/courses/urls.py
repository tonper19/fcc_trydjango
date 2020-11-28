from django.urls import path
from .views import (
    CourseView,
    CourseListView,
    CourseCreateView,
    # MyListView,
    # my_fbv
)

app_name = "courses"
urlpatterns = [
    path('', CourseListView.as_view(), name="courses-list"),
    # path('', MyListView.as_view(), name="courses-list"),
    # path("", my_fbv, name="courses-list")

    path("create/", CourseCreateView.as_view(), name="courses-create"),
    path("<int:id>/", CourseView.as_view(), name="courses-detail"),
    # path("<int:id>/update/", <update_view>, name="courses-update"),
    # path("<int:id>/delete/", <delete_view>, name="courses-delete"),

]
