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
from .forms import ArticleModelForm


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '/'  # where to go in case of success option 1

    # where to go in case of success option 2
    # on this case to detail view
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # where to go in case of success option 3
    # def get_success_url(self) -> str:
    #     return '/'


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    # looks for <blog>/<modulename>_list.html otherwise put template_name as above
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    # this may be a subset, in this case we are retreiving all data
    # queryset = Article.objects.all()

    # to override pk argument on the urls.py by the id:
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    # def get_object(self):
    #     title_ = self.kwargs.get("title")
    #     return get_object_or_404(Article, title=title_)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '/'  # where to go in case of success option 1

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    # where to go in case of success option 2
    # on this case to detail view
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # where to go in case of success option 3
    # def get_success_url(self) -> str:
    #     return '/'
