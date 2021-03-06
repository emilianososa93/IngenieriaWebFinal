from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import logout
from . import views

urlpatterns = [
	url(r'^$', views.post_portada, name='post_portada'),
	url(r'', include('blog.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^post/portada/', views.post_portada, name ='post_portada'),
    url(r'^accounts/login/$', views.post_login, name ='post_login' ),
    url(r'^post/logout/$', views.post_logout, name ='post_logout' ),
    url(r'^post/validation/$', views.post_validation, name = 'post_validation'),
    url(r'^post/confirmar/(?P<tokenActivacion>\w+)/', views.post_confirmar),
    url(r'^post/bienvenida/(?P<tokenActivacion>\w+)/', views.post_confirmar),
]