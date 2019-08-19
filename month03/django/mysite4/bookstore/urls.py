from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^setcookie$', views.set_cookies_view),

]