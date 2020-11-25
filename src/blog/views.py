from django.shortcuts import render
# 2020-11-24
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    # looks for <blog>/<modulename>_list.html otherwise put template_name as above
    queryset = Article.objects.all()
