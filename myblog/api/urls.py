from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/(?P<pk>\d+)/remove/$', views.blog_remove, name='blog_remove'),
    url(r'^blog/(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),
    url(r'^blog/(?P<pk>\d+)/edit/$', views.blog_edit, name='blog_edit'),
    url(r'^blog/new/$', views.blog_new, name='blog_new'),
    url(r'^$', views.blog_list, name='blog_list'),
]