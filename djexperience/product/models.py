from django.db import models


class Brand(models.Model):
    brand = models.CharField('marca', max_length=50, unique=True)

    class Meta:
        ordering = ['brand']
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

    def __str__(self):
        return self.brand


class TypeProduct(models.Model):
    type_product = models.CharField(
        'tipo de produto', max_length=50, unique=True)

    class Meta:
        ordering = ['type_product']
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'

    def __str__(self):
        return self.type_product
