from django.conf.urls import url

from . import views

urlpatterns= [
	url(r'^$', views.index, name='index'),
	url('^ajax/', views.ajax, name='ajax'),
]