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
