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


class Seller(Person, TimeStampedModel):
    internal = models.BooleanField('interno')
    commissioned = models.BooleanField('comissionado', default=True)
    commission = models.DecimalField(
        'comissão', max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'
