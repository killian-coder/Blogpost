from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^create/$', views.post_create),
    url(r'^detail/$', views.post_detail),
    url(r'^update/$', views.post_update),
    url(r'^delete/$', views.post_delete),
    #url(r'^$', "posts.views.post_home"),

]