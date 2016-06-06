from django.test import TestCase
from django.utils import timezone
from django.shortcuts import resolve_url as r
from djexperience.bookstore.models import Customer


class CustomerDetailTest(TestCase):

    def setUp(self):
        self.obj = Customer.objects.create(
            first_name='Adam',
            last_name='Smith',
            email='adam@example.com',
            birthday=timezone.now()
        )
        self.resp = self.client.get(
            r('bookstore:customer_detail', pk=self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'bookstore/customer_detail.html')

    def test_context(self):
        ''' Customer must be in context '''
        customer = self.resp.context['customer']
        self.assertIsInstance(customer, Customer)

    def test_html(self):
        self.assertContains(self.resp, 'Adam Smith')
        self.assertContains(self.resp, 'adam@example.com')
        self.assertContains(self.resp, 'True')


class CustomerDetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get(r('bookstore:customer_detail', pk='0'))
        self.assertEqual(404, response.status_code)
