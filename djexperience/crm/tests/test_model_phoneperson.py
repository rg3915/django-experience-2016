from django.test import TestCase
from djexperience.crm.models import PhonePerson, Person
from .data import PERSON_DICT


class PhonePersonTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(**PERSON_DICT)
        phone = PhonePerson(
            phone='11 98765-4321',
            person=self.person,
            phone_type='pri'
        )
        phone.save()

    def test_create(self):
        self.assertTrue(PhonePerson.objects.exists())
