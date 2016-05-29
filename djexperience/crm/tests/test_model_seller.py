from datetime import datetime
from django.test import TestCase
from djexperience.crm.models import Seller, Occupation
from .data import EMPLOYEE_DICT


class SellerTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(occupation='Gerente')
        self.obj = Seller.objects.create(
            occupation=self.occupation,
            **EMPLOYEE_DICT)

    # def test_create(self):
    #     self.assertTrue(Seller.objects.exists())

    def test_created(self):
        ''' Seller must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('regis', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['username'], Seller._meta.ordering)
