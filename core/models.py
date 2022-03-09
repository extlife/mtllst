from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='images', blank=True)

    def get_absolute_url(self):
        return reverse('core:product', args=[self.slug])

class Item(models.Model):
    text = models.CharField(max_length=250, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
        related_name='items')

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    text = HTMLField()
    added = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='images', blank=True)
    video = models.TextField(blank=True)
    as_cover = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('core:post', args=[self.slug])