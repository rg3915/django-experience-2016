from django.contrib import admin
from .models import Company, Contact, Status, Proposal


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'companytype')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'company', 'is_completed')


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('code', 'company', 'price')
