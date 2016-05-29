from django.test import TestCase
from djexperience.crm.models import PhoneEmployee, Employee
from .data import EMPLOYEE_DICT


class PhoneEmployeeTest(TestCase):

    def setUp(self):
        self.employee = Employee.objects.create(**EMPLOYEE_DICT)
        phone = PhoneEmployee(
            phone='11 98765-4321',
            employee=self.employee,
            phone_type='pri'
        )
        phone.save()

    def test_create(self):
        self.assertTrue(PhoneEmployee.objects.exists())
