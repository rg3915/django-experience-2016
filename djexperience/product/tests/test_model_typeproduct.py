from django.test import TestCase
from djexperience.product.models import TypeProduct


class TypeProductTest(TestCase):

    def setUp(self):
        self.obj = TypeProduct.objects.create(type_product='papelaria')

    def test_create(self):
        self.assertTrue(TypeProduct.objects.exists())

    def test_str(self):
        self.assertEqual('papelaria', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['type_product'], TypeProduct._meta.ordering)
