from django.shortcuts import render , get_object_or_404
from blog.models import ArticleModel
from .models import User
from django.urls import reverse_lazy
from .forms  import ProfileForm
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from .mixins import FieldMixin , FormValidMixin , AuthoraccessMixins , SuperUserAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ArticleList(LoginRequiredMixin,ListView) :
    template_name = 'registration/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser :
            return ArticleModel.objects.all()
        else:
            return ArticleModel.objects.filter(auth=self.request.user)

class ArticleCreate(LoginRequiredMixin,FormValidMixin,FieldMixin,CreateView):
    model = ArticleModel
    template_name = 'registration/article_create_update.html'

class ArticleUpdate(AuthoraccessMixins,FormValidMixin,FieldMixin,UpdateView):
    model = ArticleModel
    template_name = 'registration/article_create_update.html'

class AticleDelete(SuperUserAccessMixin,DeleteView):
    model = ArticleModel
    template_name = 'registration/article_delete.html'
    success_url = reverse_lazy('account:home')

class Profile(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'registration/Profile.html'
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)