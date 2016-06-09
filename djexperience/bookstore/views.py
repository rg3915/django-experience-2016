from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, get_object_or_404
from .models import Customer, Book
from .forms import CustomerForm, BookForm
from .mixins import NameSearchMixin


def home(request):
    return render(request, 'bookstore_index.html')


def customer_list(request):
    q = request.GET.get('search_box')
    if q:
        customers = Customer.objects.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q))
    else:
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


class BookList(NameSearchMixin, ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['count_published'] = Book.objects.published().count()
        return context


class BookDetail(DetailView):
    model = Book
    context_object_name = 'book'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
