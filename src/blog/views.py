from django.shortcuts import render, get_object_or_404
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


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # looks for <blog>/<modulename>_list.html otherwise put template_name as above

    # this may be a subset, in this case we are retreiving all data
    # queryset = Article.objects.all()

    # to override pk argument on the urls.py by the id:
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)
    def get_object(self):
        title_ = self.kwargs.get("title")
        return get_object_or_404(Article, title=title_)
# The Cretan Chronicles
