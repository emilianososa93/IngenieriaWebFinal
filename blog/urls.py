from django.conf.urls import  url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
		url(r'^$', views.post_portada, name='post_portada'),
		url(r'^post/$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/detail/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^post/registro/$', views.post_registro.as_view(), name ='post_registro'),
        url(r'^post/secciones/$', views.post_secciones, name ='post_secciones'),
        url(r'^post/validation/$', views.post_validation, name = 'post_validation'),
        url(r'^post/bienvenida/(?P<tokenActivacion>\w+)/', views.post_confirmar, name = 'post_bienvenida'),
]