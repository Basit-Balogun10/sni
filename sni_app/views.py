from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'sni_app/home.html')
    # return HttpResponse('View is working')
