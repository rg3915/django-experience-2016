import json
import xlwt
from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.views.generic import CreateView, ListView, DetailView
from .models import Employee, Provider, Customer, Seller
from .forms import EmployeeForm, ProviderForm


def home(request):
    return render(request, 'crm_index.html')


employee_list = ListView.as_view(model=Employee)


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.slug = e.username
            e.is_staff = True
            e.set_password(form.cleaned_data['password'])
            e.save()
            return render(request, 'index.html')
    else:
        form = EmployeeForm()
    return render(request, 'crm/employee_form.html', {'form': form})


class CustomerList(ListView):
    model = Customer


customer_detail = DetailView.as_view(model=Customer)


def customer_json(request):
    customers = Customer.objects.all()
    json = serializers.serialize('json', customers)
    return HttpResponse(json, content_type='application/json')


def customer_list_by_json(request):
    customers = Customer.objects.all()
    data_as_json = serializers.serialize('json', customers)
    data_as_dict = json.loads(data_as_json)
    data_as_dict = {'mydict': data_as_dict}
    return render(request, 'crm/customer_json2.html', context=data_as_dict)


def customer_json_render(request):
    return render(request, 'crm/customer_json.html')


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="customers.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Customers')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nome', 'Sobrenome', 'E-mail', 'Nascimento', 'Criado em']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    default_style = xlwt.XFStyle()

    rows = Customer.objects.all().values_list('first_name',
                                              'last_name',
                                              'email',
                                              'birthday',
                                              'created')
    for row, rowdata in enumerate(rows):
        row_num += 1
        for col, val in enumerate(rowdata):
            if isinstance(val, datetime):
                val = val.strftime('%d/%m/%Y %H:%M')
            elif isinstance(val, date):
                val = val.strftime('%d/%m/%Y')
            ws.write(row_num, col, val, default_style)

    wb.save(response)
    return response


class ProviderCreate(CreateView):
    model = Provider
    form_class = ProviderForm


provider_list = ListView.as_view(model=Provider)

seller_list = ListView.as_view(model=Seller)
