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


class Product(models.Model):
    imported = models.BooleanField('importado', default=False)
    outofline = models.BooleanField('fora de linha', default=False)
    perishable = models.BooleanField('perecível', default=False)
    ncm = models.CharField('NCM', max_length=8)
    brand = models.ForeignKey('Brand', verbose_name='marca')
    product = models.CharField('produto', max_length=60, unique=True)
    short_description = models.TextField('descrição curta', blank=True)
    description = models.TextField('descrição completa', blank=True)
    cost = models.DecimalField('custo', max_digits=6, decimal_places=2)
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)
    icms = models.DecimalField(
        'ICMS', max_digits=3, decimal_places=2, blank=True)
    ipi = models.DecimalField(
        'IPI', max_digits=3, decimal_places=2, blank=True)
    stock_min = models.PositiveIntegerField('Estoque mínimo', default=0)
    stock = models.IntegerField('Estoque atual')

    class Meta:
        ordering = ['product']
        verbose_name = u'produto'
        verbose_name_plural = u'produtos'

    def __str__(self):
        return self.product
