from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'sni_app/home.html')
    # return HttpResponse('View is working')


def organizer(request):
    return render(request, 'sni_app/organizer.html')
    # return HttpResponse('Organizer View is working')


def schedule(request):
    return render(request, 'sni_app/schedule.html')
    # return HttpResponse('Schedule View is working')


def speakers(request):
    return render(request, 'sni_app/speakers.html')
    # return HttpResponse('Speakers View is working')


def sponsors(request):
    return render(request, 'sni_app/sponsors.html')
    # return HttpResponse('Sponsors View is working')


def venue(request):
    return render(request, 'sni_app/venue.html')
    # return HttpResponse('Venue View is working')
