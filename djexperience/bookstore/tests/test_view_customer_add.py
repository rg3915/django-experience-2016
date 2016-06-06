from django.test import TestCase
from django.utils import timezone
from django.shortcuts import resolve_url as r
from djexperience.bookstore.forms import CustomerForm
from djexperience.bookstore.models import Customer


class CustomerAddGet(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('bookstore:customer_add'))

    def test_get(self):
        ''' GET /customer/add/ must return status code 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        ''' Must use bookstore/customer_form.html '''
        self.assertTemplateUsed(self.resp, 'bookstore/customer_form.html')

    def test_html(self):
        ''' Html must contain input tags '''
        tags = (('<form', 1),
                ('<input', 5),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        ''' Html must contain csrf '''
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        ''' Context must have customer form '''
        form = self.resp.context['form']
        self.assertIsInstance(form, CustomerForm)


class CustomerAddPostValid(TestCase):

    def setUp(self):
        data = dict(
            first_name='Adam',
            last_name='Smith',
            email='adam@example.com',
            birthday=timezone.now()
        )
        self.resp = self.client.post(r('bookstore:customer_add'), data)

    def test_post(self):
        ''' Valid POST should redirect to /customer_detail/1/ '''
        self.assertRedirects(self.resp, r('bookstore:customer_detail', 1))

    def test_save_customer(self):
        self.assertTrue(Customer.objects.exists())


class CustomerAddPostInvalid(TestCase):

    def setUp(self):
        self.resp = self.client.post(r('bookstore:customer_add'), {})

    def test_post(self):
        ''' Invalid POST should not redirect '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'bookstore/customer_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, CustomerForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_customer(self):
        self.assertFalse(Customer.objects.exists())


class TemplateRegressionTest(TestCase):

    def test_template_has_non_field_errors(self):
        invalid_data = dict(name='Adam Smith', email='adam')
        response = self.client.post(r('bookstore:customer_add'), invalid_data)
        self.assertContains(response, '<ul class="errorlist nonfield">')
