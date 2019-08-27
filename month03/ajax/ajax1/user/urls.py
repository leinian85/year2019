from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^xhr$',views.xhr ,name='xhr'),
    url(r'^get-xhr$',views.get_xhr,name='get_xhr'),
    url(r'^get-xhr-server$',views.get_xhr_server ,name='get_xhr_server'),
    url(r'^xhr_regist$',views.xhr_regist ,name='xhr_regist'),
    url(r'^regist$',views.regist ,name='regist'),
    url(r'^login$',views.login ,name='login'),
    url(r'^regist_post$',views.regist_post ,name='regist_post'),
    url(r'^index$',views.index ,name='index'),
    url(r'^$',views.index ,name='index'),
    url(r'^show$',views.show ,name='show'),
    url(r'^json_dumps$',views.json_dumps ,name='json_dumps'),

]