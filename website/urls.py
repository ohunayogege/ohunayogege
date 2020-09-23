from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^blog$', views.blog, name='blog'),
	url(r'^blog/(?P<slug>[\w-]+)$', views.blogview, name='blogview'),

	url(r'^ajax-contact/$', views.ajax_contact, name='ajax_contact'),# ajax-posting / name = that we will use in ajax url
]