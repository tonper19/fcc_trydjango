from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # this is the standard: use pk as the argument on a DetailView
    #    path('<int:pk>', ArticleDetailView.as_view(), name='article-detail')
    # to override the standard pk arg, in the views.py,
    #    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    path('<str:title>', ArticleDetailView.as_view(), name='article-detail'),
]
