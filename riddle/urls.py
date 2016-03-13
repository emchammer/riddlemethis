from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.riddle_one, name = 'riddle_one'),
    url(r'^key$', views.riddle_two,name = 'riddle_two'),
    url(r'^88$', views.riddle_three, name = 'riddle_three'),
    url(r'^infinity$', views.riddle_four, name='riddle_four'),
]
