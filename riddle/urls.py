from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.riddle_one, name = 'riddle_one'),
    url(r'^8$', views.riddle_two,name = 'riddle_two'),
]
