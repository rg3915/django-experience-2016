from django.db import models
from djexperience.core.models import TimeStampedModel


class Service(models.Model):
    ''' Serviço '''
    title = models.CharField('serviço', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'


class TypeService(models.Model):
    ''' Tipo de Serviço '''
    title = models.CharField('tipo', max_length=100, unique=True)
    service = models.ForeignKey(Service, verbose_name='serviço')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'tipo de serviço'
        verbose_name_plural = 'tipos de serviços'


class Protest(TimeStampedModel):
    ''' Reclamação '''
    typeservice = models.ForeignKey(
        TypeService,
        verbose_name='tipo de serviço'
    )
    description = models.TextField('Descrição')

    def __str__(self):
        return 'Reclamação #{}'.format(self.pk)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'reclamação'
        verbose_name_plural = 'reclamações'

    def get_absolute_url(self):
        return r('service:protest_detail', pk=self.pk)
