from django.conf.urls import include, url
from djexperience.company import views as co
from djexperience.company import exports as exp

company_patterns = [
    url(r'^$', co.company_list, name='company_list'),
    url(r'^export/$', exp.export_data_contact, name='export_data_contact'),
]

urlpatterns = [
    url(r'^company/', include(company_patterns)),
]
