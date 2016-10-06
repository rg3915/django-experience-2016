from django.views.generic import CreateView
from .models import Product
from .forms import ProductForm


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
