from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Appointment, Clown
from .forms import AppointmentForm, ClownForm
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def index(request):
    clowns = Clown.objects.all()
    appoints = Appointment.objects.all()
    if request.method == 'POST':
        form = ClownForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = ClownForm()

    context = {
        'clowns': clowns,
        'form': form,
        'appoints': appoints,
    }
    return render(request, 'clownApp/dashboard/index.html', context)


@login_required
def appointment(request):
    items = Appointment.objects.all()
    clients_count = User.objects.all().count()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            appointment_clown = form.cleaned_data.get('clown')
            messages.success(request, f'Appointment for {appointment_clown} has been added')
            return redirect('dashboard-appointment')
    else:
        form = AppointmentForm()

    context = {
        'items': items,
        'form': form,
        'clients_count': clients_count,
    }
    return render(request, 'clownApp/dashboard/appointment.html', context)


@login_required
def appointment_delete(request, pk):
    item = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-appointment')
    return render(request, 'clownApp/dashboard/appointment_delete.html')


@login_required
def appointment_update(request, pk):
    item = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-appointment')
    else:
        form = AppointmentForm()

    context = {'form': form}
    return render(request, 'clownApp/dashboard/appointment_update.html', context)


@login_required
def client(request):
    clients = User.objects.all()
    clients_count = clients.count()

    context = {
        'clients': clients,
        'clients_count': clients_count,
    }
    return render(request, 'clownApp/dashboard/client.html', context)


@login_required
def client_detail(request, pk):
    clients = User.objects.get(id=pk)

    context = {'clients': clients}
    return render(request, 'clownApp/dashboard/client_detail.html', context)


@login_required
def clown(request):
    clowns = Clown.objects.all()
    clients_count = User.objects.all().count()

    context = {
        'clowns': clowns,
        'clients_count': clients_count,
    }
    return render(request, 'clownApp/dashboard/clown.html', context)




