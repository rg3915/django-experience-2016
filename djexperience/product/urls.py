from django.conf.urls import include, url
from djexperience.product import views as p

product_patterns = [
    url(r'^add/$', p.ProductCreate.as_view(), name='product_add'),
]

urlpatterns = [
    url(r'^product/', include(product_patterns)),
]
