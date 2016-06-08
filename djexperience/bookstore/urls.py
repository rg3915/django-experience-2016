from django.conf.urls import include, url
from .views import home, customer_list, customer_detail, customer_form

customer_patterns = [
    url(r'^$', customer_list, name='customer_list'),
    url(r'^(?P<pk>\d+)/$', customer_detail, name='customer_detail'),
    url(r'^add/$', customer_form, name='customer_add'),
]

urlpatterns = [
    url(r'^$', home, name='bookstore_index'),
    url(r'^customer/', include(customer_patterns)),
]
