from django.test import TestCase
from django.utils import timezone
from djexperience.bookstore.forms import CustomerForm


class CustomerFormTest(TestCase):

    def test_form_has_fields(self):
        ''' Form must have 4 fields '''
        form = CustomerForm()
        expected = ['first_name', 'last_name', 'email', 'birthday']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_first_name_must_be_capitalized(self):
        ''' First_name must be capitalized. '''
        form = self.make_validated_form(name='Adam')
        self.assertEqual('Adam', form.cleaned_data['first_name'])

    def test_last_name_must_be_capitalized(self):
        ''' Last_name must be capitalized. '''
        form = self.make_validated_form(name='Adam')
        self.assertEqual('Smith', form.cleaned_data['last_name'])

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(
            first_name='Adam',
            last_name='Smith',
            email='adam@example.com',
            birthday=timezone.now()
        )
        data = dict(valid, **kwargs)
        form = CustomerForm(data)
        form.is_valid()
        return form
