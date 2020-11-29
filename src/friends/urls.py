from django.urls import path
from .views import (
    FriendCreateView,
    FriendListView,
    FriendDetailView,
    FriendUpdateView,
    FriendDeleteView,
)

app_name = 'friends'
urlpatterns = [

    path('', FriendListView.as_view(), name='friend-list'),
    path('create/', FriendCreateView.as_view(), name='friend-create'),
    path('<int:id>', FriendDetailView.as_view(), name='friend-detail'),
    path('<int:id>/update/', FriendUpdateView.as_view(), name='friend-update'),
    path('<int:id>/delete/', FriendDeleteView.as_view(), name='friend-delete'),

    # this is the standard: use pk as the argument on a DetailView
    # path('<int:pk>', ArticleDetailView.as_view(), name='article-detail')
    # to override the standard pk arg, in the views.py,
    # to override by using a string (no spaces between words):
    #path('<str:title>', ArticleDetailView.as_view(), name='article-detail'),
]
