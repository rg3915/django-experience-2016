from django.db import models
from djexperience.utils.lists import COMPANY_TYPE


class Company(models.Model):
    name = models.CharField(max_length=50)
    companytype = models.CharField(max_length=1, choices=COMPANY_TYPE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(Company, related_name='contact_company')

    class Meta:
        ordering = ['company', 'name']

    def __str__(self):
        return self.name


class Status(models.Model):
    status = models.CharField(max_length=10)
    company = models.ForeignKey(Company, related_name='status_company')
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['company', 'status']

    def __str__(self):
        return self.status


class Proposal(models.Model):
    code = models.CharField(max_length=10)
    company = models.ForeignKey(Company, related_name='proposal_company')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['company', 'code']

    def __str__(self):
        return self.code
