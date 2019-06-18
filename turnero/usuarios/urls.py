# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns =[
	url(r'^salir/$', views.UserLogoutView.as_view(), name='logout'),
]
