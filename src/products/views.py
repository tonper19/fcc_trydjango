from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {'title': obj.title,
    #            'description': obj.description,
    #            'price': obj.price,
    #            }
    context = {
        'object': obj
    }
    # return render(request, "product/detail.html", context)
    # using in App template
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    initial_data = {
        "title": "Initial title",
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,
                       initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../../")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

# def product_create_view(request):
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get("title")
#         print(my_new_title)

#     context = {}
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             # pass dictionary as a bunch of arguments
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)

#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)
