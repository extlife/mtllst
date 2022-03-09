from django.contrib import admin
from .models import Product, Item, Post

# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0
    min_num = 1

@admin.register(Product)
class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ItemInline]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'added')
    date_hierarchy = 'added'
    ordering = ('added',)
