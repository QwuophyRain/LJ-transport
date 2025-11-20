from django.contrib import admin
from.models import Drivers

# Register your models here.

class DriversAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'national_id',]
    list_filter = ['first_name']

admin.site.register(Drivers, DriversAdmin)
