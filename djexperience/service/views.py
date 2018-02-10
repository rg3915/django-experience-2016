from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Protest, TypeService
from .forms import ProtestForm


class ProtestList(ListView):
    model = Protest
    paginate_by = 10


class ProtestCreate(CreateView):
    model = Protest
    form_class = ProtestForm
    success_url = reverse_lazy('service:protest_list')


class ProtestDetail(DetailView):
    model = Protest


def load_typeservices(request):
    service_id = request.GET.get('service')
    typeservices = TypeService.objects.filter(service_id=service_id)
    typeservices = typeservices.order_by('title')
    kw = {'typeservices': typeservices}
    return render(request, 'service/_include_typeservice_list_options.html', kw)
