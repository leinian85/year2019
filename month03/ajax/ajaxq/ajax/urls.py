from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^load$', views.load),
    url(r'^load_server$', views.load_server),
    url(r'^jquery_get/$', views.jquery_get),
    url(r'^jquery_get_server/$', views.jquery_get_server),
    url(r'^jquery_post/$', views.jquery_post),
    url(r'^jquery_post_server/$', views.jquery_post_server),
    url(r'^jquery_ajax/$', views.jquery_ajax),
    url(r'^jquery_ajax_server/$', views.jquery_ajax_server),
    url(r'^ajax_list/$', views.ajax_list),
    url(r'^ajax_list_server/$', views.ajax_list_server),
    url(r'^cross/$', views.cross),
    url(r'^cross_server/$', views.cross_server),
]
