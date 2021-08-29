from django.shortcuts import render


def index(request):
    return render(request, 'clownApp/dashboard/index.html')


def client(request):
    return render(request, 'clownApp/dashboard/client.html')


def clown(request):
    return render(request, 'clownApp/dashboard/clown.html')


def appointment(request):
    return render(request, 'clownApp/dashboard/appointment.html')

