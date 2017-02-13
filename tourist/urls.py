#coding=utf-8

from django.conf.urls import url
from tourist import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^detail/', views.tourist, name="detail"),
]