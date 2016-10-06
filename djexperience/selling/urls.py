from django.conf.urls import include, url
from djexperience.selling import views as s

selling_patterns = [
    url(r'^add/$', s.selling_form, name='selling_add'),
]

urlpatterns = [
    url(r'^selling/', include(selling_patterns)),
]
