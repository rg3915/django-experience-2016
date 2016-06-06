from django.conf.urls import url
from .views import customer_list

urlpatterns = [
    url(r'^customer_list', customer_list, name='customer_list'),
]
