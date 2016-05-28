from django.contrib import admin
from .models import Person, PhonePerson, Occupation, Customer
from .models import Employee, PhoneEmployee, Seller, Provider


class PhonePersonInline(admin.TabularInline):
    model = PhonePerson
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [PhonePersonInline]
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ['__str__', 'email', 'active']
    search_fields = ('first_name', 'last_name')


class PhoneEmployeeInline(admin.TabularInline):
    model = PhoneEmployee
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [PhoneEmployeeInline]
    list_display = ['__str__', 'email', 'occupation', 'active']
    search_fields = ('first_name', 'last_name')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'occupation']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'active']
    search_fields = ('first_name', 'last_name')


admin.site.register(Customer)
admin.site.register(Occupation)
