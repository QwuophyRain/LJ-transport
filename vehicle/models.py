from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea, FileInput
from embed_video.fields import EmbedVideoField
from django.utils.safestring import mark_safe
from django.utils.crypto import get_random_string



# Create your models here.
class Vehicles(models.Model):
    STATUS = (

        ('Healthy', 'Healthy'),
        ('Needs Servicing', 'Needs Servicing'),
        ('Needs Repairs', 'Needs Repairs'),
        ('Other', 'Other'),
    )

    FUEL = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('LPG', 'LPG'),
        ('Propane', 'Propane'),
        ('Gasoline', 'Gasoline'),
        ('Ethanol', 'Ethanol'),
        ('CNG', 'CNG'),
        ('Hybrid', 'Hybrid'),
        ('Biodiesel', 'Biodiesel'),
        ('Fuel Oil', 'Fuel Oil'),
        ('Electricity', 'Electricity'),
        ('Other', 'Other'),
    )

    TYPE = (
        ('Coach / Motor', 'Coach / Motor'),
        ('Coach', 'Coach'),
        ('School Bus', 'School Bus'),
        ('Shuttle', 'Shuttle'),
        ('Minibus', 'Minibus'),
        ('MiniCoach', 'MiniCoach'),
        ('Single-decker', 'Single-decker'),
        ('Double-decker', 'Double-decker'),
        ('Low-floor', 'Low-floor'),
        ('Other', 'Other'),
    )

    bus_name = models.CharField(blank=True, max_length=100)
    bus_type = models.CharField(max_length=20, choices=TYPE, default='Double-decker')
    color = models.CharField(max_length=50)
    capacity = models.FloatField(default=0)
    cost_per_day = models.FloatField(default=0)
    registration_plate = models.CharField(blank=True, max_length=50)
    bus_status = models.CharField(max_length=20, choices=STATUS, default='Healthy')
    insurance_status = models.ImageField(blank=True, upload_to='image/insurance', default='insure.png')
    speed = models.FloatField(default=0)
    fuel_type = models.CharField(max_length=25, choices=FUEL, default='petrol')
    is_available = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='image/vehicles', default='car.png',)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bus_name

    class Meta:
        verbose_name_plural = 'Vehicles'



class VehicleForm(ModelForm):
    class Meta:
        model = Vehicles
        fields = ['bus_name', 'bus_type', 'color', 'capacity', 'cost_per_day', 'registration_plate', 'bus_status',
                  'insurance_status', 'speed', 'fuel_type', 'is_available', 'image']
        widgets = {
            'bus_name': TextInput(attrs={'class': 'input', 'placeholder': 'Name'}),
            'bus_type': TextInput(attrs={'class': 'input', 'placeholder': 'Bus Type'}),
            'color': TextInput(attrs={'class': 'input', 'placeholder': 'Color'}),
            'capacity': TextInput(attrs={'class': 'input', 'placeholder': 'capacity'}),
            'cost_per_day': TextInput(attrs={'class': 'input', 'placeholder': 'Cost per day'}),
            'registration_plate': TextInput(attrs={'class': 'input', 'placeholder': 'Plate number'}),
            'bus_status': TextInput(attrs={'class': 'input', 'placeholder': 'Bus Status'}),
            'fuel_type': TextInput(attrs={'class': 'input', 'placeholder': 'Fuel Type'}),
            'is_available': TextInput(attrs={'class': 'input', 'placeholder': 'Availability'}),
            'insurance_status': FileInput(attrs={'style': 'display: none;', 'class': 'form-control', 'required': False}),
            'image': FileInput(attrs={'style': 'display: none;', 'class': 'form-control', 'required': False}),

        }
