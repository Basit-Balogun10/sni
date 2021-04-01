from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('organizer', views.organizer, name='organizer'),
    path('speakers', views.speakers, name='speakers'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('venue', views.venue, name='venue'),
]
