from django.urls import path
from . import views
from personal.views import (
    home_screen_view,
)
from account.views import (ActivateAccount, ResendActivationEmail, VerifyNewEmail, ChangeEmail, )

app_name = 'sni_app'

urlpatterns = [
    path('', views.home, name='sni_home'),
    path('schedule', views.schedule, name='schedule'),
    # path('synergyhub', views.synergy_hub, name='synergy-hub'),
    path('about', views.about, name='about'),
    path('organizer', views.organizer, name='organizer'),
    path('speakers', views.speakers, name='speakers'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('venue', views.venue, name='venue'),
    
    path('resend_activation_email/<uidb64>/<token>/<target>', ResendActivationEmail.as_view(), name='resend'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('verify_new_email/<uidb64>/<token>/<to>', VerifyNewEmail.as_view(), name='verify_new_email'),
    path('email_change', ChangeEmail.as_view(), name='email_change'),
]
