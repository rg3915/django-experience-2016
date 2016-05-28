from django.contrib import admin
from .models import Person, Occupation, PhonePerson, Customer, Employee, Seller


class PhonePersonInline(admin.TabularInline):
    model = PhonePerson
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhonePersonInline]
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ('__str__', 'email', 'active')
    search_fields = ('first_name', 'last_name')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'occupation']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'occupation']

admin.site.register(Customer)
admin.site.register(Occupation)
