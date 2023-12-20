# validationApp/urls.py
from django.urls import path
from .views import participant_form, vehicle_form, success

urlpatterns = [
    path('', participant_form, name='participant_form'),
    path('vehicle/', vehicle_form, name='vehicle_form'),
    path('success/', success, name='success'),
]
