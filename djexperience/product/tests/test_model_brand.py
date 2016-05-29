from django.test import TestCase
from djexperience.product.models import Brand


class BrandTest(TestCase):

    def setUp(self):
        self.obj = Brand.objects.create(brand='philco')

    def test_create(self):
        self.assertTrue(Brand.objects.exists())

    def test_str(self):
        self.assertEqual('philco', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['brand'], Brand._meta.ordering)
