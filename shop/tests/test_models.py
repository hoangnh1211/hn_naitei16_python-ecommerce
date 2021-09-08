from django.test import TestCase
from django.urls import reverse
from shop.models import CustomUser, Image, Item, Order, Product,Category, ProductSize, Size, Comment, Sale, SaleProduct
from ..utils.constant import LENGTH_PAGE, STATUS_ORDER, FILTER, SALE


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name= "Category test 1", description= "Description for category test 1")

    def test_get_absolute_url_category(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/category/1/')

    def test_category_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_category_description_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('description').max_length
        self.assertEqual(max_length, 254)


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name= "Category test 1", description= "Description for category test 1")
        product = Product.objects.create(name= "Product test 1", category= category, price= 500000.0, description= 'Description for product test 1')

    def test_get_absolute_url_product(self):
        product = Product.objects.get(id=3)
        self.assertEqual(product.get_absolute_url(), '/product/3')

    def test_add_to_cart_url_product(self):
        product = Product.objects.get(id=3)
        self.assertEqual(product.get_add_to_cart_url(), '/add_to_cart/3')

    def test_object_name_product(self):
        product = Product.objects.get(id=3)
        expected_object_name = product.name
        self.assertEqual(str(product), expected_object_name)

    def test_product_name_max_length(self):
        product = Product.objects.get(id=3)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = CustomUser.objects.create_user(email= 'test1@gmail.com', username='testuser1', password='1X<ISRUkw+tuK')
        obj = Order.objects.create(user = test_user1, status = STATUS_ORDER['waitting'])

    def test_get_cancel_order_url(self):
        obj = Order.objects.get(id=2)
        self.assertEqual(obj.get_cancel_order_url(), '/cancel_order/2')


class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = CustomUser.objects.create_user(email= 'test1@gmail.com', username='testuser1', password='1X<ISRUkw+tuK')
        obj = Order.objects.create(user = test_user1, status = STATUS_ORDER['not_paid'])
        category = Category.objects.create(name= "Category test 2", description= "Description for category test 2")
        product = Product.objects.create(name= "Product test 2", category= category, price= 500000.0, description= 'Description for product test 2')
        size = Size.objects.create(description='XL')
        item = Item.objects.create(order = obj, product = product, size = size)

    def test_amount_defaults_item(self):
        item = Item.objects.get(id=1)
        expected_amout_item = item.amount
        self.assertEqual(expected_amout_item, 0)

    def test_get_remove_cart_url(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.get_remove_cart_url(), '/remove_cart/1')

    def test_get_update_cart_url(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.get_update_cart_url(), '/update_cart/1')


class SaleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        sale = Sale.objects.create(value= 50.0, url= "jum5_3.jpg", description= "Description for sale test 1")

    def test_sale_url_max_length(self):
        sale = Sale.objects.get(id=1)
        max_length = sale._meta.get_field('url').max_length
        self.assertEqual(max_length, 254)

    def test_sale_description_max_length(self):
        sale = Sale.objects.get(id=1)
        max_length = sale._meta.get_field('description').max_length
        self.assertEqual(max_length, 254)


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = CustomUser.objects.create_user(email= 'test1@gmail.com', username='testuser1', password='1X<ISRUkw+tuK')
        category = Category.objects.create(name= "Category test 2", description= "Description for category test 2")
        product = Product.objects.create(name= "Product test 2", category= category, price= 500000.0, description= 'Description for product test 2')
        comment = Comment.objects.create(user= test_user1, product= product, content= "Content for commnet test 1")

    def test_comment_content_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('content').max_length
        self.assertEqual(max_length, 254)


class SizeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        size = Size.objects.create(description= 'Description for size test 1')

    def test_size_description_max_length(self):
        size = Size.objects.get(id=2)
        max_length = size._meta.get_field('description').max_length
        self.assertEqual(max_length, 254)
