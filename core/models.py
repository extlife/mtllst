from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250, unique=True,
        verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True,
        verbose_name='URL')
    image = models.ImageField(upload_to='images', blank=True,
        verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('core:product', args=[self.slug])

class Item(models.Model):
    text = models.CharField(max_length=250, blank=True, null=True,
        verbose_name = 'Наименование')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
        related_name='items')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Изделия'

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True,
        verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique=True,
        verbose_name='URL')
    text = HTMLField(verbose_name='Текст')
    added = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='images', blank=True,
        verbose_name='Обложка')

    def get_absolute_url(self):
        return reverse('core:post', args=[self.slug])

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
