from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .models import Company, Contact, Status, Proposal


CONTACTFIELDS = ('treatment', 'name', 'birthday', 'created')


class ContactResource(resources.ModelResource):
    treatment = fields.Field(
        attribute='get_treatment_display',
        column_name='treatment'
    )
    age = fields.Field()

    class Meta:
        model = Contact
        fields = CONTACTFIELDS
        export_order = CONTACTFIELDS
        widgets = {
            'next_contact': {'format': '%d/%m/%Y'},
            'created': {'format': '%d/%m/%Y %H:%M'},
        }

    def dehydrate_age(self, obj):
        return obj.get_age()


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource
    list_display = ('name', 'company', 'email', 'phone')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'companytype')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'company', 'is_completed')


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('code', 'company', 'price')
