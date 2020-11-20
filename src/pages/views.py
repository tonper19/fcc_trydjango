from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    print(f'Calling {__name__}.home_view() ...')
    print(f'request.user: {request.user}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    print(f'Calling {__name__}.contact_view() ...')
    print(f'request.user: {request.user}')
    # return HttpResponse("<h1>Contact View</h1>")
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    print(f'Calling {__name__}.about_view() ...')
    print(f'request.user: {request.user}')
    # return HttpResponse("<h1>Contact View</h1>")
    return render(request, "about.html", {})
