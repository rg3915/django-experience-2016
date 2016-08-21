from django.shortcuts import render
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


class ProviderCreate(CreateView):
    model = Provider
    form_class = ProviderForm

provider_list = ListView.as_view(model=Provider)

seller_list = ListView.as_view(model=Seller)
