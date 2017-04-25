''' Exporta planilhas em Excel '''
from datetime import datetime
from django.http import HttpResponse
from import_export.admin import ExportMixin
from import_export.formats.base_formats import XLSX

from djexperience.company.models import Contact
from djexperience.company.admin import ContactResource


MDATA = datetime.now().strftime('%Y-%m-%d')


def _export_data(queryset, model, filename_prefix, resource_class):
    e = ExportMixin()
    e.resource_class = resource_class
    e.model = model
    data = e.get_export_data(XLSX(), queryset)
    response = HttpResponse(
        data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response[
        'Content-Disposition'] = 'attachment; filename="{0}-{1}.xlsx"'.format(filename_prefix, MDATA)
    return response


def export_data_contact(request):
    queryset = Contact.objects.all()
    model = Contact
    filename_prefix = 'contatos'
    resource_class = ContactResource
    return _export_data(queryset, model, filename_prefix, resource_class)
