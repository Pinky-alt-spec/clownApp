from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm


@login_required
def index(request):
    return render(request, 'clownApp/dashboard/index.html')


@login_required
def appointment(request):
    items = Appointment.objects.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-appointment')
    else:
        form = AppointmentForm()

    context = {
        'items': items,
        'form': form,
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
        item.delete()
        return redirect('dashboard-appointment')
    return render(request, 'clownApp/dashboard/appointment_update.html')


@login_required
def client(request):
    return render(request, 'clownApp/dashboard/client.html')


@login_required
def clown(request):
    return render(request, 'clownApp/dashboard/clown.html')




