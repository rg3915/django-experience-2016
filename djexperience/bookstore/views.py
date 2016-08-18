from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, get_object_or_404
import django_excel as excel
from django.http import HttpResponseBadRequest
from .models import Customer, Book, Author
from .forms import CustomerForm, BookForm
from .mixins import NameSearchMixin


def home(request):
    return render(request, 'bookstore_index.html')


def export_data(request, atype):
    if atype == "sheet":
        return excel.make_response_from_a_table(
            Customer, 'xls', file_name="sheet")
    elif atype == "custom":
        query_sets = Customer.objects.all()
        column_names = ['first_name', 'last_name', 'email', 'birthday']
        return excel.make_response_from_query_sets(
            query_sets,
            column_names,
            'xls',
            file_name="custom"
        )
    else:
        return HttpResponseBadRequest(
            "Bad request. please put one of these " +
            "in your url suffix: sheet, book or custom")


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


author_list = ListView.as_view(model=Author)

author_detail = DetailView.as_view(model=Author)

author_create = CreateView.as_view(
    model=Author, fields=['name'], success_url=reverse_lazy('bookstore:author_list'))
