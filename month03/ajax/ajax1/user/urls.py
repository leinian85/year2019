from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^xhr$',views.xhr ,name='xhr'),
    url(r'^get-xhr$',views.get_xhr,name='get_xhr'),
    url(r'^get-xhr-server$',views.get_xhr_server ,name='get_xhr_server'),
    url(r'^xhr_regist$',views.xhr_regist ,name='xhr_regist'),
    url(r'^regist$',views.regist ,name='regist'),
    url(r'^login$',views.login ,name='login'),

]