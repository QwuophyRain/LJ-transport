from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .models import Vehicles, VehicleForm
from home.models import Settings




# Create your views here.
def index(request):
    return HttpResponse("vehicle")

@login_required(login_url='/login')   # shopping for only members
def addVehicles(request):
    if request.method == 'POST':  # check post
        form = VehicleForm(request.POST)
        if form.is_valid():
            data = Vehicles()  # create relation with mode
            data.bus_name = form.cleaned_data['bus_name']
            data.bus_type = form.cleaned_data['bus_type']
            data.cost_per_day = form.cleaned_data['cost_per_day']
            data.color = form.cleaned_data['color']
            data.capacity = form.cleaned_data['capacity']
            data.registration_plate = form.cleaned_data['registration_plate']
            data.bus_status = form.cleaned_data['bus_status']
            data.insurance_status = form.cleaned_data['insurance_status']
            data.speed = form.cleaned_data['speed']
            data.fuel_type = form.cleaned_data['fuel_type']
            data.is_available = form.cleaned_data['is_available']
            if len(request.FILES) != 0:
                data.image = request.FILES['image']
                data.insurance_status = request.FILES['insurance_status']
            data.save()  # save data to table
            messages.success(request, "Vehicle Successfully Added.")  # flash message
            return HttpResponseRedirect('/vehicle_list')  # redirect to home page after submitting comment

        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/new_vehicle')

    setting = Settings.objects.get(pk=1)
    vehicles = Vehicles.objects.all().order_by('?')[:6]
    context = {'setting': setting, 'vehicles': vehicles}
    return render(request, 'new_vehicle.html', context)


def vehicleList(request):
    setting = Settings.objects.get(pk=1)
    vehicles = Vehicles.objects.all().order_by('-id')[:9]

    context = {'setting': setting, 'vehicles': vehicles}
    return render(request, 'vehicle_list.html', context)


@login_required(login_url='/login')
def delete_vehicle(request, pk):
    vehicles = Vehicles.objects.get(id=pk)
    if request.method == 'POST':
        vehicles.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/vehicle_list')
    return render(request, 'delete_vehicle.html')


@login_required(login_url='/login')
def updateVehicles(request, pk):
    buses = Vehicles.objects.get(id=pk)

    if request.method == 'POST':
        # check if image is not empty
        if len(request.FILES) != 0:
            # if len(vehicle.image) > 0:
            #     os.remove(vehicle.image.path)
            buses.image = request.FILES['image']
        buses.bus_name = request.POST.get('buses')
        buses.bus_type = request.POST.get('bus_type')
        buses.color = request.POST.get('color')
        buses.capacity = request.POST.get('capacity')
        buses.cost_per_day = request.POST.get('cost_per_day')
        buses.registration_plate = request.POST.get('registration_plate')
        buses.bus_status = request.POST.get('bus_status')
        buses.insurance_status = request.POST.get('insurance_status')
        buses.speed = request.POST.get('speed')
        buses.fuel_type = request.POST.get('fuel_type')
        buses.is_available = request.POST.get('is_available')
        buses.save()
        messages.success(request, 'Successfully Updated')
        return redirect('/')

    setting = Settings.objects.get(pk=1)

    context = {
        'buses': buses, 'setting': setting,
    }
    return render(request, 'update_vehicle.html', context)
