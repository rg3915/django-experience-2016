from django.shortcuts import render
from .models import Customer


def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'bookstore/customer_list.html', context)
