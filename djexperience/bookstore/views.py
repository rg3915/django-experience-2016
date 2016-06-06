from django.shortcuts import render, get_object_or_404
from .models import Customer


def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'bookstore/customer_list.html', context)


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {'customer': customer}
    return render(request, 'bookstore/customer_detail.html', context)
