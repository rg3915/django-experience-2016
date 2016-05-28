from datetime import datetime
from django.test import TestCase
from djexperience.crm.models import Person, Occupation
from .data import PERSON_DICT


class PersonTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(occupation='Gerente')
        self.obj = Person.objects.create(
            occupation=self.occupation, **PERSON_DICT)

    def test_create(self):
        self.assertTrue(Person.objects.exists())

    def test_created(self):
        ''' Person must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Sr. Regis Santos', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['first_name'], Person._meta.ordering)
