# validationApp/views.py
from django.shortcuts import render, redirect
from .forms import ParticipantForm, VehicleForm
from .models import Vehicle
from django.http import HttpResponse
import logging

logger = logging.getLogger('my_logger')

def my_view(request):
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    return HttpResponse("Hello, world!")

def participant_form(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ParticipantForm()
    return render(request, 'participant_form.html', {'form': form})

def vehicle_form(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = VehicleForm()
    return render(request, 'vehicle_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
    vehicles = Vehicle.objects.all()
    return render(request, 'success.html', {'vehicles': vehicles})


