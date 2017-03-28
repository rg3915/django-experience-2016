from django.conf.urls import include, url
from djexperience.company import views as co

company_patterns = [
    url(r'^$', co.company_list, name='company_list'),
]

urlpatterns = [
    url(r'^company/', include(company_patterns)),
]
