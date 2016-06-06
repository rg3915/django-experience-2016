from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('djexperience.core.urls', namespace='core')),
    url(r'^bookstore/', include('djexperience.bookstore.urls', namespace='bookstore')),
    url(r'^admin/', admin.site.urls),
]
