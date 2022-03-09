from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/<slug:slug>', views.product, name='product'),
    path('news/', views.news, name='news'),
    path('news/<slug:slug>', views.post, name='post'),
    path('about', views.about, name='about'),
    path('geo', views.geo, name='geo'),
    path('payment', views.payment, name='payment'),
    path('price', views.price, name='price'),
    path('feedback', views.feedback, name='feedback'),
]