from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('djexperience.core.urls', namespace='core')),
    url(r'^bookstore/', include('djexperience.bookstore.urls', namespace='bookstore')),
    url(r'^crm/', include('djexperience.crm.urls', namespace='crm')),
    url(r'^product/', include('djexperience.product.urls', namespace='product')),
    url(r'^selling/', include('djexperience.selling.urls', namespace='selling')),
    url(r'^admin/', admin.site.urls),
]
