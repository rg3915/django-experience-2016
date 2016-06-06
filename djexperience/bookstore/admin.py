from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Author, Book, People, PF, PJ, Customer, Provider
from .models import Sale, Ordered


class CustomerResource(resources.ModelResource):

    class Meta:
        model = Customer


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'email', 'active')
    search_fields = ('first_name', 'last_name')
    list_filter = ('active',)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(People)
admin.site.register(PF)
admin.site.register(PJ)
admin.site.register(Provider)
admin.site.register(Sale)
admin.site.register(Ordered)
