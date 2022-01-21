from unicodedata import category

from django.shortcuts import render , get_object_or_404
from .models import ArticleModel , CategoryModel
from django.views.generic import ListView , DetailView
from account.models import User
from account.mixins import AuthoraccessMixins
# Create your views here.
class ArticleList(ListView):
    paginate_by = 4
    queryset = ArticleModel.objects.filter(status='publish')

class ArticleDetail(DetailView):
    template_name = 'blog/detail.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ArticleModel , pk=pk)

class CategoryList(ListView):
    template_name = 'blog/category_list.html'
    paginate_by = 4
    def get_queryset(self):
        global category
        pk = self.kwargs.get('pk')
        category = get_object_or_404(CategoryModel , pk=pk)
        return category.childrens.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

class AuthorList(ListView):
    template_name = 'blog/author.html'
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User , username=username)
        return author.author.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['auth'] = author
        return context

class Preview(AuthoraccessMixins,DetailView):
    template_name = 'blog/detail.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ArticleModel , pk=pk)