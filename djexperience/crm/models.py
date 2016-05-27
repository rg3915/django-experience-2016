from django.db import models
from djexperience.core.models import Address, TimeStampedModel


class Person(Address):
    first_name = models.CharField('nome', max_length=50)
    last_name = models.CharField('sobrenome', max_length=50)
    email = models.EmailField()
    active = models.BooleanField('ativo', default=True)
    blocked = models.BooleanField('bloqueado')

    class Meta:
        abstract = True


class Customer(Person):
    pass

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


class Employee(Person):
    occupation = models.ForeignKey(
        'Occupation', verbose_name='cargo', related_name='employee_occupation',
        null=True, blank=True)
    internal = models.BooleanField('interno')
    commissioned = models.BooleanField('comissionado', default=True)
    commission = models.DecimalField(
        'comissão', max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'

    def __str__(self):
        return self.first_name


class Occupation(models.Model):
    occupation = models.CharField('cargo', max_length=50, unique=True)

    class Meta:
        ordering = ['occupation']
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'

    def __str__(self):
        return self.occupation


class SellerManager(models.Manager):

    def get_queryset(self):
        return super(SellerManager, self).get_queryset()\
            .filter(occupation__occupation='Vendedor')


class Seller(Employee):
    objects = SellerManager()

    class Meta:
        proxy = True
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'

    def __str__(self):
        return self.first_name
