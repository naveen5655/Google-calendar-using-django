from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url('/calebdar', views.CalendarView.as_view(), name='calendar'),
    url('', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
