from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# 2020-11-24
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Friend
from .forms import FriendModelForm


class FriendCreateView(CreateView):
    template_name = 'friends/friend_create.html'
    form_class = FriendModelForm
    queryset = Friend.objects.all()
    # success_url = '/'  # where to go in case of success option 1

    # where to go in case of success option 2
    # on this case to detail view
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # where to go in case of success option 3
    # def get_success_url(self) -> str:
    #     return '/'


class FriendListView(ListView):
    template_name = 'friends/friend_list.html'
    # looks for <friends>/<modulename>_list.html otherwise put template_name as above
    queryset = Friend.objects.all()


class FriendDetailView(DetailView):
    template_name = 'friends/friend_detail.html'

    # this may be a subset, in this case we are retreiving all data
    # queryset = Friend.objects.all()

    # to override pk argument on the urls.py by the id:
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Friend, id=id_)
    # def get_object(self):
    #     name_ = self.kwargs.get("name")
    #     return get_object_or_404(Friend, name=name_)


class FriendUpdateView(UpdateView):
    template_name = 'friends/friend_create.html'
    form_class = FriendModelForm
    queryset = Friend.objects.all()
    # success_url = '/'  # where to go in case of success option 1

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Friend, id=id_)

    # where to go in case of success option 2
    # on this case to detail view
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # where to go in case of success option 3
    # def get_success_url(self) -> str:
    #     return '/'


class FriendDeleteView(DeleteView):
    template_name = 'friends/friend_delete.html'

    # this may be a subset, in this case we are retreiving all data
    # queryset = Friend.objects.all()

    # to override pk argument on the urls.py by the id:
    def get_object(self):
        id_ = self.kwargs.get("id")
        print(f"*** friends FriendDeleteView get object: {id_}")
        return get_object_or_404(Friend, id=id_)

    def get_success_url(self) -> str:
        url = reverse('friends:friend-list')
        print(f"*** friends FriendDeleteView get_success_url: {url}")
        return url
