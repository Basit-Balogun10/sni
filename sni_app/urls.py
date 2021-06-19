from django.urls import path
from . import views
from personal.views import (
    home_screen_view,
)

app_name = 'sni_app'

urlpatterns = [
    path('', views.home, name='sni_home'),
    path('schedule', views.schedule, name='schedule'),
    path('synergyhub', views.synergy_hub, name='synergy-hub'),
    path('about', views.about, name='about'),
    path('organizer', views.organizer, name='organizer'),
    path('speakers', views.speakers, name='speakers'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('venue', views.venue, name='venue'),
]
