from django.contrib import admin
from.models import Vehicles

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['bus_name', 'bus_type', 'registration_plate', 'cost_per_day']
    list_filter = ['bus_name']

admin.site.register(Vehicles, VehicleAdmin)
