from django.conf.urls import  url, include
from . import views


urlpatterns = [
    url(r'^$', views.books_list, name='home'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^book/new/$', views.book_new, name='book_new'),
    url(r'^book/(?P<pk>[0-9]+)/edit/$', views.book_edit, name='book_edit'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.delete, name='book_delete'),
]