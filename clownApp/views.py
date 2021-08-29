from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


@login_required
def index(request):
    return render(request, 'clownApp/dashboard/index.html')


@login_required
def client(request):
    return render(request, 'clownApp/dashboard/client.html')


@login_required
def clown(request):
    return render(request, 'clownApp/dashboard/clown.html')


@login_required
def appointment(request):
    return render(request, 'clownApp/dashboard/appointment.html')

