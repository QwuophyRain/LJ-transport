from django.contrib import admin
from.models import Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'bus', 'start_date', 'end_date']
    list_filter = ['user']

admin.site.register(Booking, BookingAdmin)