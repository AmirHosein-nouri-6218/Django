from django.http import Http404
from blog.models import ArticleModel
from django.shortcuts import get_object_or_404

class FieldMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser :
            self.fields = ['auth', 'title', 'slug', 'category', 'description', 'thumbnail', 'publish','is_special','status']
        elif request.user.is_author :
            self.fields = [ 'title', 'slug', 'category', 'description', 'thumbnail', 'publish','is_special']
        else :
            raise Http404('page not found...')
        return super().dispatch(request,*args,**kwargs)


class FormValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser :
            form.save()
        else :
            self.obj = form.save(commit=False)
            self.obj.auth = self.request.user
            self.obj.status = 'draft'
        return super().form_valid(form)

class AuthoraccessMixins():
    def dispatch(self,request,pk,*args,**kwargs):
        article = get_object_or_404(ArticleModel , pk=pk)
        if article.auth == request.user and article.status in ['back','draft'] or request.user.is_superuser  :
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404('Error Access...')

class SuperUserAccessMixin():
    def dispatch(self,request,pk,*args,**kwargs):
        article = get_object_or_404(ArticleModel , pk=pk)
        if request.user.is_superuser or article.auth == request.user and article.status == 'draft':
            return super().dispatch(request,*args,**kwargs)
        else :
            raise Http404("Error Access...")