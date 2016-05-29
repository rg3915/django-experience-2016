from django.test import TestCase
from djexperience.product.models import Brand, Product
from .data import PRODUCT_DICT


class TypeProductTest(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(brand='Philco')
        self.obj = Product.objects.create(brand=self.brand, **PRODUCT_DICT)

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_str(self):
        self.assertEqual('Smart TV LED 40" Philco Ultra 4K', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['product'], Product._meta.ordering)
