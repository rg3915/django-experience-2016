from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import Protest
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
