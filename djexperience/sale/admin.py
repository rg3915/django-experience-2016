from django.contrib import admin
from .models import Customer, Ordered, Sale


admin.site.register(Customer)
admin.site.register(Ordered)
admin.site.register(Sale)
