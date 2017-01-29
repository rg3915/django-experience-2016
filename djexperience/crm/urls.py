from django.conf.urls import include, url
from djexperience.crm import views as c

employee_patterns = [
    url(r'^$', c.employee_list, name='employee_list'),
    url(r'^add/$', c.employee_create, name='employee_add'),
]

customer_patterns = [
    url(r'^$', c.CustomerList.as_view(), name='customer_list'),
    url(r'^json/$', c.customer_json, name='customer_json'),
    url(r'^json2/$', c.customer_list_by_json, name='customer_json2'),
    url(r'^render/$', c.customer_json_render, name='customer_json_render'),
    url(r'^(?P<slug>[\w-]+)/$', c.customer_detail, name='customer_detail'),
]

provider_patterns = [
    url(r'^$', c.provider_list, name='provider_list'),
    url(r'^add/$', c.ProviderCreate.as_view(), name='provider_add'),
]

seller_patterns = [
    url(r'^$', c.seller_list, name='seller_list'),
]

urlpatterns = [
    url(r'^$', c.home, name='crm_index'),
    url(r'^employee/', include(employee_patterns)),
    url(r'^customer/', include(customer_patterns)),
    url(r'^provider/', include(provider_patterns)),
    url(r'^seller/', include(seller_patterns)),
]
