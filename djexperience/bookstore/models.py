from django.db import models


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
        verbose_name_plural = 'pessoas física'

    def __str__(self):
        return self.first_name


class PJ(People):
    cnpj = models.CharField('CNPJ', max_length=50, blank=True)
    ie = models.CharField('IE', max_length=50, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'pessoa jurídica'
        verbose_name_plural = 'pessoas jurídica'

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
