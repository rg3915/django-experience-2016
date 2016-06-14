from django.test import TestCase
from django.utils import timezone
from django.shortcuts import resolve_url as r
from djexperience.bookstore.models import Customer


class CustomerListTest(TestCase):

    def setUp(self):
        self.obj = Customer.objects.create(
            first_name='Ad4m',
            last_name='Sm1th',
            email='adam@example.com',
            birthday=timezone.now()
        )
        self.resp = self.client.get(r('bookstore:customer_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'bookstore/customer_list.html')

    def test_html(self):
        contents = [
            (1, 'Ad4m Sm1th'),
            (1, 'adam@example.com'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_full_name(self):
        ''' Must have full name '''
        expected = ' '.join(filter(None, ['Ad4m', 'Sm1th']))
        self.assertEqual(expected, self.obj.full_name)


class CustomerListGetEmpty(TestCase):

    def test_get_empty(self):
        response = self.client.get(r('bookstore:customer_list'))
        self.assertContains(response, 'Sem itens na lista')
