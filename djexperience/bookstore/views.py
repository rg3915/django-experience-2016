from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Customer
from .forms import CustomerForm


def home(request):
    return render(request, 'bookstore_index.html')


def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'bookstore/customer_list.html', context)


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {'customer': customer}
    return render(request, 'bookstore/customer_detail.html', context)


def customer_form(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    return render(request, 'bookstore/customer_form.html',
                  {'form': CustomerForm()})


def create(request):
    form = CustomerForm(request.POST)
    if not form.is_valid():
        return render(request, 'bookstore/customer_form.html', {'form': form})

    obj = form.save()
    return HttpResponseRedirect('/bookstore/customer/%d/' % obj.pk)
