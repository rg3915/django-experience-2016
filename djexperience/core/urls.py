from django.conf.urls import url
from djexperience.core.views import home


urlpatterns = [
    url(r'^$', home, name='home'),
]
