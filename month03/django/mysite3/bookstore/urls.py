from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^index$',views.index),
    url(r'^insert$',views.insert),
    url(r'^add_author$',views.add_author),
    url(r'^show_book$',views.show_book),
    url(r'^show_author$',views.show_author),
    url(r'^serach$',views.serach),
    url(r'^delete$',views.book_delete),
    url(r'^update_book$',views.update_book),
]