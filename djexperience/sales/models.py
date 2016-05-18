from django.db import models

METHOD_PAID = [
    ('vi', 'a vista'),
    ('bo', 'boleto'),
    ('ch', 'cheque'),
    ('de', 'débito'),
    ('cr', 'crédito'),
]

STATUS_LIST = (
    ('c', 'cancelado'),
    ('p', 'pendente'),
    ('a', 'aprovado')
)


class Sale(models.Model):
    ordered = models.OneToOneField('Ordered', verbose_name='pedido')
    paid = models.BooleanField('pago')
    date_paid = models.DateField('data da pagamento')
    method_paid = models.CharField(
        'forma da pagamento', max_length=2, choices=METHOD_PAID)
    deadline = models.CharField('prazo de entrega', max_length=50)


class Ordered(models.Model):
    customer = models.ForeignKey('Customer', verbose_name='cliente')
    status_ordered = models.CharField(
        'status', max_length=2, choices=STATUS_LIST)
