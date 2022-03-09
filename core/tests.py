from django.test import TestCase
from django.core import mail
from django.test import override_settings
from .models import Product, Item, Post

# Create your tests here.

class PagesTest(TestCase):

    def test_home_page_return_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/home.html')
    
    def test_products_page_return_correct_html(self):
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'core/products.html')
    
    def test_product_page_return_correct_html(self):
        product = Product.objects.create(title='Some product',
            slug='some_product')
        response = self.client.get(f'/products/{product.slug}')
        self.assertTemplateUsed(response, 'core/product.html')

    def test_news_page_return_correct_html(self):
        response = self.client.get('/news/')
        self.assertTemplateUsed(response, 'core/news.html')

    def test_about_page_return_correct_html(self):
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'core/about.html')
    
    def test_geo_page_return_correct_html(self):
        response = self.client.get('/geo')
        self.assertTemplateUsed(response, 'core/geo.html')

    def test_payment_page_return_correct_html(self):
        response = self.client.get('/payment')
        self.assertTemplateUsed(response, 'core/payment.html')

    def test_price_page_return_correct_html(self):
        response = self.client.get('/price')
        self.assertTemplateUsed(response, 'core/price.html')


class ProductTest(TestCase):
    
    def test_saving_and_retrieving_product(self):
        product_1 = Product.objects.create(title='Title one',
            slug='title_one')

        product_2 = Product.objects.create(title='Title two',
            slug='title_two')

        saved_items = Product.objects.all()
        self.assertEqual(saved_items.count(), 2)

        saved_item_1 = saved_items[0]
        saved_item_2 = saved_items[1]

        self.assertEqual(saved_item_1.title, 'Title one')
        self.assertEqual(saved_item_2.title, 'Title two')

    def test_saving_and_retrieving_product_item(self):
        product_1 = Product.objects.create(title='Title one',
            slug = 'title_one')
        item_1 = Item.objects.create(text='item 1', product=product_1)
        item_2 = Item.objects.create(text='item 2',product=product_1)

        product_2 = Product.objects.create(title='Title two',
            slug='title_two')
        item_3 = Item.objects.create(text='item 3', product=product_2)
        item_4 = Item.objects.create(text='item 4', product=product_2)

        saved_product_1 = Product.objects.first()
        saved_product_2 = Product.objects.last()

        saved_items = Item.objects.all()

        self.assertEqual(saved_items.count(), 4)

        saved_item_1 = saved_items[0]
        saved_item_2 = saved_items[1]
        saved_item_3 = saved_items[2]
        saved_item_4 = saved_items[3]

        self.assertEqual(saved_item_1.text, 'item 1')
        self.assertEqual(saved_item_2.text, 'item 2')
        self.assertEqual(saved_item_3.text, 'item 3')
        self.assertEqual(saved_item_4.text, 'item 4')

        self.assertNotIn(saved_item_1, saved_product_2.items.all())
        self.assertNotIn(saved_item_2, saved_product_2.items.all())
        self.assertNotIn(saved_item_3, saved_product_1.items.all())
        self.assertNotIn(saved_item_4, saved_product_1.items.all())


class PostTest(TestCase):
    def test_saving_and_retrieving_post(self):
        Post.objects.create(title='Some title', text='Some text')
        saved_post = Post.objects.first()
        self.assertEqual(saved_post.title, 'Some title')


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class EmailTest(TestCase):
    
    def test_user_send_mail(self):
        self.client.post('/feedback', data={
            'name': 'Guest',
            'phone': '1234567890',
            'email': 'gues@example.com',
            'text': 'Here is the message.'
        })
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Here is the message.', mail.outbox[0].body)
        self.assertIn('Gues', mail.outbox[0].body)
        self.assertIn('1234567890', mail.outbox[0].body)
