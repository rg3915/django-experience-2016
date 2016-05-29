from django.db import models
from djexperience.core.models import TimeStampedModel
from djexperience.utils.lists import STATUS_LIST, METHOD_PAID


class Author(models.Model):
    name = models.CharField('nome', max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('nome', max_length=50)
    authors = models.ManyToManyField('Author', verbose_name='autores')

    class Meta:
        ordering = ['name']
        verbose_name = 'livro'
        verbose_name_plural = 'livros'

    def __str__(self):
        return self.name


class People(models.Model):
    first_name = models.CharField('nome', max_length=50)
    last_name = models.CharField('sobrenome', max_length=50)
    email = models.EmailField()

    class Meta:
        ordering = ['first_name']
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

    def __str__(self):
        return self.first_name


class PF(People):
    rg = models.CharField('RG', max_length=50, blank=True)
    cpf = models.CharField('CPF', max_length=50, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'pessoa física'
        verbose_name_plural = 'pessoas físicas'

    def __str__(self):
        return self.first_name


class PJ(People):
    cnpj = models.CharField('CNPJ', max_length=50, blank=True)
    ie = models.CharField('IE', max_length=50, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'pessoa jurídica'
        verbose_name_plural = 'pessoas jurídicas'

    def __str__(self):
        return self.first_name


class Customer(People):
    pass

    class Meta:
        ordering = ['first_name']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


class Provider(People):
    books = models.ManyToManyField('Book', verbose_name='livros')
    price = models.DecimalField('preço', max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'


class Ordered(TimeStampedModel):
    customer = models.ForeignKey('Customer', verbose_name='cliente')
    status_ordered = models.CharField(
        'status', max_length=2, choices=STATUS_LIST)

    class Meta:
        ordering = ['-created']
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'


class Sale(TimeStampedModel):
    ordered = models.OneToOneField('Ordered', verbose_name='pedido')
    paid = models.BooleanField('pago')
    date_paid = models.DateField('data da pagamento')
    method_paid = models.CharField(
        'forma da pagamento', max_length=2, choices=METHOD_PAID)
    deadline = models.CharField('prazo de entrega', max_length=50)

    class Meta:
        ordering = ['-created']
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'
