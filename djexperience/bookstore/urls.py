from django.conf.urls import include, url
from djexperience.bookstore import views as b

customer_patterns = [
    url(r'^$', b.customer_list, name='customer_list'),
    url(r'^(?P<pk>\d+)/$', b.customer_detail, name='customer_detail'),
    url(r'^add/$', b.customer_form, name='customer_add'),
]

book_patterns = [
    url(r'^$', b.BookList.as_view(), name='book_list'),
    url(r'^(?P<pk>\d+)/$', b.BookDetail.as_view(), name='book_detail'),
    url(r'^(?P<pk>\d+)/edit/$', b.BookUpdate.as_view(), name='book_edit'),
    url(r'^add/$', b.BookCreate.as_view(), name='book_add'),
]

urlpatterns = [
    url(r'^$', b.home, name='bookstore_index'),
    url(r'^customer/', include(customer_patterns)),
    url(r'^book/', include(book_patterns)),
]
