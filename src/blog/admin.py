from django.contrib import admin
from .models import CategoryModel , ArticleModel
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent','title','slug','position','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
admin.site.register(CategoryModel,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('auth','title','picture','slug','publish','status','category_list')
    list_filter = ('publish','status')
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
admin.site.register(ArticleModel,ArticleAdmin)