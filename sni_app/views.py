from django.shortcuts import render

from account.forms import AccountAuthenticationForm
from django.http import HttpResponse


# Create your views here.


def home(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        quick_login = True
        login_form = AccountAuthenticationForm()
        context['login_form'] = login_form
        context['quick_login'] = quick_login
    return render(request, 'sni_app/home.html', context)
    # return HttpResponse('View is working')


def about(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        quick_login = True
        login_form = AccountAuthenticationForm()
        context['login_form'] = login_form
        context['quick_login'] = quick_login
    return render(request, 'sni_app/about.html', context)
    # return HttpResponse('Organizer View is working')


def organizer(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        quick_login = True
        login_form = AccountAuthenticationForm()
        context['login_form'] = login_form
        context['quick_login'] = quick_login
    return render(request, 'sni_app/organizer.html', context)
    # return HttpResponse('Organizer View is working')


# def synergy_hub(request):
#     return render(request, 'sni_app/synergy_hub.html')
#     # return HttpResponse('Schedule View is working')


def schedule(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        quick_login = True
        login_form = AccountAuthenticationForm()
        context['login_form'] = login_form
        context['quick_login'] = quick_login
    return render(request, 'sni_app/schedule.html', context)
    # return HttpResponse('Schedule View is working')


def speakers(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        quick_login = True
        login_form = AccountAuthenticationForm()
        context['login_form'] = login_form
        context['quick_login'] = quick_login
    return render(request, 'sni_app/speakers.html', context)
    # return HttpResponse('Speakers View is working')


def sponsors(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        quick_login = True
        login_form = AccountAuthenticationForm()
        context['login_form'] = login_form
        context['quick_login'] = quick_login
    return render(request, 'sni_app/sponsors.html', context)
    # return HttpResponse('Sponsors View is working')


def venue(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        quick_login = True
        login_form = AccountAuthenticationForm()
        context['login_form'] = login_form
        context['quick_login'] = quick_login
    return render(request, 'sni_app/venue.html', context)
    # return HttpResponse('Venue View is working')
