from django.conf.urls import url

from . import views

urlpatterns= [
	url(r'^$', views.Dashboard.as_view(), name='index'),
	url('^ajax/', views.Dashboard.ajax, name='ajax'),
]
