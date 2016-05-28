from datetime import datetime
from django.test import TestCase
from djexperience.crm.models import Employee, Occupation
from .data import EMPLOYEE_DICT


class EmployeeTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(occupation='Gerente')
        self.obj = Employee.objects.create(
            occupation=self.occupation,
            **EMPLOYEE_DICT)

    def test_create(self):
        self.assertTrue(Employee.objects.exists())

    def test_created(self):
        ''' Employee must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('regis', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['username'], Employee._meta.ordering)
