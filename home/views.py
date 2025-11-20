from django.shortcuts import render
from .models import *
from vehicle.models import Vehicles
from booking.models import Booking, OrderBus
from driver.models import Drivers




# Create your views here.
def index(request):
    setting = Settings.objects.get(pk=1)
    buses = Vehicles.objects.all().order_by('-id')
    count_vehicles = Vehicles.objects.all().count()
    count_bookings = Booking.objects.all().count()
    count_orders = OrderBus.objects.all().count()
    count_drivers = Drivers.objects.all().count()
    context = {'setting': setting, 'buses': buses, 'count_vehicles': count_vehicles,
               'count_bookings': count_bookings, 'count_drivers': count_drivers, 'count_orders': count_orders}
    return render(request, 'index.html', context)