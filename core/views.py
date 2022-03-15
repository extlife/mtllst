from django.shortcuts import render, redirect,  get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Product, Post
from .forms import FeedbackForm

# Create your views here.

def home(request):
    products = Product.objects.all()[:3]
    return render(request, 'core/home.html', {'products': products})

def products(request):
    products = Product.objects.all()
    return render(request, 'core/products.html', {'products': products})

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'core/product.html', {'product': product})

def news(request):
    posts = Post.objects.order_by('-added')
    return render(request, 'core/news.html', {'posts': posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'core/post.html', {'post': post})

def about(request):
    return render(request, 'core/about.html')

def geo(request):
    return render(request, 'core/geo.html')

def payment(request):
    return render(request, 'core/payment.html')

def price(request):
    return render(request, 'core/price.html')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f'[MTLLST] User {cd["name"]} send mail'
            message = render_to_string('core/email.html', {'data': cd})
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER])
            messages.info(request, 'Сообщение успешно отправлено')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
        return redirect(request.POST.get('next'))
    return redirect('/')
