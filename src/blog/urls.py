from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = 'articles'
urlpatterns = [

    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

    # this is the standard: use pk as the argument on a DetailView
    # path('<int:pk>', ArticleDetailView.as_view(), name='article-detail')
    # to override the standard pk arg, in the views.py,
    # to override by using a string (no spaces between words):
    #path('<str:title>', ArticleDetailView.as_view(), name='article-detail'),
]
