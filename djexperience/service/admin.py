from django.contrib import admin
from .models import Service, TypeService, Protest


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('title',)


@admin.register(TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'service')
    search_fields = ('title',)


@admin.register(Protest)
class ProtestAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'service',
        'type_service',
    )
    search_fields = (
        'typeservice__service__title',
        'typeservice__title',
    )
    list_filter = ('typeservice__service', )

    def service(self, obj):
        return obj.typeservice.service
    service.admin_order_field = 'title'
    service.short_description = 'Serviço'

    def type_service(self, obj):
        return obj.typeservice
    type_service.admin_order_field = 'title'
    type_service.short_description = 'Tipo de Serviço'
