from django.conf.urls import include, url
from djexperience.crm import views as c

employee_patterns = [
    url(r'^add/$', c.employee_create, name='employee_add'),
]

provider_patterns = [
    url(r'^add/$', c.ProviderCreate.as_view(), name='provider_add'),
]

urlpatterns = [
    url(r'^employee/', include(employee_patterns)),
    url(r'^provider/', include(provider_patterns)),
]
