from django.db import models
from django.utils.timezone import now
from djexperience.utils.lists import COMPANY_TYPE, STATUS_LIST, TREATMENT
from djexperience.core.models import TimeStampedModel


class Company(TimeStampedModel):
    name = models.CharField(max_length=50)
    companytype = models.CharField(max_length=1, choices=COMPANY_TYPE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    treatment = models.CharField(
        'tratamento', max_length=4, choices=TREATMENT, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(Company, related_name='contact_company')
    birthday = models.DateField('nascimento', null=True, blank=True)

    class Meta:
        ordering = ['company', 'name']

    def __str__(self):
        return self.name

    def get_age(self):
        # Retorna a idade da pessoa
        today = now().date()
        bdate = self.birthday

        if not bdate:
            return 0

        age = today.year - bdate.year

        # Verifica se o dia e o mês de aniversário já passaram;
        # se não, tira 1 de `age`.
        if today.month < bdate.month \
           or (today.month == bdate.month and today.day < bdate.day):
            age -= 1

        return age


class Status(models.Model):
    status = models.CharField(max_length=1, choices=STATUS_LIST)
    company = models.ForeignKey(Company, related_name='status_company')
    next_contact = models.DateField('próximo contato', null=True, blank=True)
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
