from django.views.generic import CreateView, ListView, DetailView
from .models import Protest
from .forms import ProtestForm


class ProtestList(ListView):
    model = Protest
    paginate_by = 10


class ProtestCreate(CreateView):
    model = Protest
    form_class = ProtestForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        userprofile = UserProfile.objects.get(user=self.request.user)
        self.object.userprofile = userprofile
        self.object.save()
        return super(ProtestCreate, self).form_valid(form)


class ProtestDetail(DetailView):
    model = Protest
