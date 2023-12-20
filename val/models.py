# validationApp/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_plate_number(value):
    # Assuming Rwandan plate number format: RXX123A (R followed by two letters, three numbers, and one letter)
    if not value.startswith('R') or not value[1:3].isalpha() or not value[3:6].isdigit() or not value[6].isalpha():
        raise ValidationError(_('Invalid Rwandan plate number format.'))
    
def validate_ur_ac_rw_email(value):
    # Check if the email domain is "ur.ac.rw"
    if not value.endswith('@ur.ac.rw'):
        raise ValidationError(_('Email must be from the "ur.ac.rw" domain.'))
    
def validate_valid_phone_number(value):
    if not value.startswith('+'):
        raise ValidationError(_('Invalid phone number format.'))
        
def validate_age_limit(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError(_('Participants must be 18 years or older.'))


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    mid_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[validate_valid_phone_number])
    date_of_birth = models.DateField(validators=[validate_age_limit])
    reference_number = models.IntegerField(validators=[MinValueValidator(99), MaxValueValidator(999)])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    vehicle = models.OneToOneField('Vehicle', on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    email = models.EmailField(validators=[validate_ur_ac_rw_email])

class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    license = models.CharField(max_length=20)
    plate_number = models.CharField(max_length=10, validators=[validate_plate_number])
    
    manufacture_date = models.DateField(default=date.today)
    
    def __str__(self):
        return f"{self.make} {self.model} - {self.plate_number}"
