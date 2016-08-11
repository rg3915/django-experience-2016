from django.conf.urls import include, url
from djexperience.crm import views as c

employee_patterns = [
    url(r'^$', c.employee_list, name='employee_list'),
    url(r'^add/$', c.employee_create, name='employee_add'),
]

customer_patterns = [
    url(r'^$', c.CustomerList.as_view(), name='customer_list'),
    url(r'^(?P<slug>[\w-]+)/$', c.customer_detail, name='customer_detail'),
]

provider_patterns = [
    url(r'^$', c.provider_list, name='provider_list'),
    url(r'^add/$', c.ProviderCreate.as_view(), name='provider_add'),
]

urlpatterns = [
    url(r'^$', c.home, name='crm_index'),
    url(r'^employee/', include(employee_patterns)),
    url(r'^customer/', include(customer_patterns)),
    url(r'^provider/', include(provider_patterns)),
]
