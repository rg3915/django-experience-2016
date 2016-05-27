from django.contrib import admin
from .models import Customer, Employee, Seller, Occupation


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'occupation']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'occupation']

admin.site.register(Customer)
admin.site.register(Occupation)
