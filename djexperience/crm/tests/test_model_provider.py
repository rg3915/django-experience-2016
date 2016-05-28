from datetime import datetime
from django.test import TestCase
from djexperience.crm.models import Provider, Occupation
from .data import PERSON_DICT


class ProviderTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(occupation='')
        self.obj = Provider.objects.create(
            occupation=self.occupation, **PERSON_DICT)

    def test_create(self):
        self.assertTrue(Provider.objects.exists())

    def test_created(self):
        ''' Provider must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Regis', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['first_name'], Provider._meta.ordering)
