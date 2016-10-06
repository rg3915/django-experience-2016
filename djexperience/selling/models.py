from django.db import models
from djexperience.core.models import TimeStampedModel
from djexperience.crm.models import Customer, Seller
from djexperience.product.models import Product


class Sale(TimeStampedModel):
    customer = models.ForeignKey(
        Customer, related_name='customer_sale', verbose_name='cliente')
    seller = models.ForeignKey(
        Seller, related_name='seller_sale', verbose_name='vendedor')

    class Meta:
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __str__(self):
        return "%03d" % self.id + "/%s" % self.created.strftime('%y')
    codigo = property(__str__)

    def get_detalhe(self):
        pass

    # conta os itens em cada venda
    def get_itens(self):
        return self.sales_det.count()

    def get_total(self):
        pass


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name='sales_det')
    product = models.ForeignKey(
        Product, related_name='product_det', verbose_name='produto')
    quantity = models.PositiveSmallIntegerField('quantidade')
    price_sale = models.DecimalField(
        'Preço de venda', max_digits=6, decimal_places=2, default=0)
    ipi_sale = models.DecimalField(
        'IPI', max_digits=3, decimal_places=2, default=0.1)

    def __str__(self):
        return str(self.sale)

    def get_subtotal(self):
        return self.price_sale * (self.quantity or 0)

    subtotal = property(get_subtotal)

    def getID(self):
        return "%04d" % self.id

    def price_sale_formated(self):
        pass

    def get_ipi(self):
        pass

    def subtotal_formated(self):
        pass
