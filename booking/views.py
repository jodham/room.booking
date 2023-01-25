from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    templatename = 'booking/index.html'
    context = {}
    return render(request, templatename, context)


def dashboard(request):
    templatename = 'booking/dashboard.html'
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, templatename, context)
