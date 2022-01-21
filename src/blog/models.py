from django.db.models.expressions import ValueRange
from django.urls import reverse
from django.db import models
from account.models import User
from django.utils import timezone
from django.utils.html import format_html

# Create your models here.
class CategoryModel(models.Model):
    parent = models.ForeignKey('self',null=True,blank=True,default=None,related_name='parents',on_delete=models.SET_NULL,verbose_name='دسته بندی')
    title = models.CharField(max_length=300,verbose_name='عنوان')
    slug = models.SlugField(max_length=50,unique=True,verbose_name='آدرس')
    position = models.IntegerField(verbose_name='پوزیشن')
    status = models.BooleanField(default=True,verbose_name='وظعیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندیها'
        ordering = ['parent__id','position']


class ArticleModel(models.Model):
    auth = models.ForeignKey(User,null=True,related_name='author',on_delete=models.SET_NULL,verbose_name='نویسنده')
    title = models.CharField(max_length=300,verbose_name='عنوان')
    slug = models.SlugField(max_length=50,unique=True,verbose_name='آدرس')
    category = models.ManyToManyField(CategoryModel,related_name='childrens',verbose_name='دسته بندی')
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(verbose_name='عکس')
    create = models.DateTimeField(auto_now=True,verbose_name='زمان ساخت')
    publish = models.DateTimeField(default=timezone.now,verbose_name='زمان ساخت')
    update = models.DateTimeField(auto_now_add=True,verbose_name='بروزرسانی در')
    STATUS = (
        ('publish','منتشر شد'),
        ('draft','پیش نویس'),
        ('investigation','درحال بررسی'),
        ('back','برگشت داده شده')
    )
    is_special = models.BooleanField(default=False,verbose_name='مقاله ویژه')
    status = models.CharField(max_length=15,choices=STATUS,verbose_name='وظعیت')

    def __str__(self):
        return self.title

    def picture(self):
        return format_html("<img height=75 style=border-radius:5px width=80 src={}>".format(self.thumbnail.url))
    picture.short_description = 'تصویر'

    def get_absolute_url(self):
        return reverse('account:home')

    def category_list(self):
        return ' ,'.join([cat.title for cat in self.category.all()])
    category_list.short_description = 'دسته بندی'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['publish']