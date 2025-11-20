from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .models import Drivers, DriverForm
from home.models import Settings
from .filters import DriverFilter
from django.core.paginator import Paginator
from datetime import datetime
import datetime
import xlwt
import json



# Create your views here.
def index(request):
    return HttpResponse("driver")


def addDriver(request):
    if request.method == 'POST':  # check post
        form = DriverForm(request.POST)
        if form.is_valid():
            data = Drivers()  # create relation with mode
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.national_id = form.cleaned_data['national_id']
            data.email = form.cleaned_data['email']
            data.phone_number = form.cleaned_data['phone_number']
            data.license_ID = form.cleaned_data['license_ID']
            data.license_category = form.cleaned_data['license_category']
            data.address = form.cleaned_data['address']
            data.photo = form.cleaned_data['photo']
            data.save()  # save data to table
            messages.success(request, "Driver Successfully Added. Thank you for your message.")  # flash message
            return HttpResponseRedirect('/driver_list')  # redirect to home page after submitting comment

        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/')

    setting = Settings.objects.get(pk=1)
    drivers = Drivers.objects.all().order_by('?')[:6]
    context = {'setting': setting, 'drivers': drivers}
    return render(request, 'new_driver.html', context)

def driverList(request):
    setting = Settings.objects.get(pk=1)
    drivers = Drivers.objects.all().order_by('-id')[:9]

    context = {'setting': setting, 'drivers': drivers}
    # filter
    filtered_driver = DriverFilter(
        request.GET,
        queryset=Drivers.objects.all().order_by('-id')
    )
    count = filtered_driver.qs.count()

    context['filtered_driver'] = filtered_driver
    context['count'] = count

    # pagination
    paginated_driver = Paginator(filtered_driver.qs, 6)
    page_number = request.GET.get('page')
    driver_page_obj = paginated_driver.get_page(page_number)

    context['driver_page_obj'] = driver_page_obj

    return render(request, 'driver_list.html', context=context)


@login_required(login_url='/login')
def delete_driver(request, pk):
    drivers = Drivers.objects.get(id=pk)
    if request.method == 'POST':
        drivers.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/driver_list')
    return render(request, 'delete_driver.html')


@login_required(login_url='/login')
def updateDrivers(request, pk):
    drivers = Drivers.objects.get(id=pk)


    if request.method == 'POST':
        # check if image is not empty
        if len(request.FILES) != 0:
            if len(drivers.image) > 0:
                os.remove(blog.photo.path)
            drivers.photo = request.FILES['photo']
        drivers.first_name = request.POST.get('first_name')
        drivers.last_name = request.POST.get('last_name')
        drivers.national_id = request.POST.get('national_id')
        drivers.email = request.POST.get('email')
        drivers.phone_number = request.POST.get('phone_number')
        drivers.license_ID = request.POST.get('license_ID')
        drivers.license_category = request.POST.get('license_category')
        drivers.save()
        messages.success(request, 'Successfully Updated')
        return redirect('/')

    setting = Settings.objects.get(pk=1)

    context = {
        'drivers': drivers, 'setting': setting,
    }
    return render(request, 'update_driver.html', context)


def exportDrivers(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Drivers' +\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Drivers Data') # this will make a sheet named drivers data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['First Name', 'Last Name', 'National ID', 'Address', 'Email', 'Phone', 'License ID', 'L. Category', 'Date Added' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Drivers.objects.all().values_list('first_name', 'last_name', 'national_id', 'address', 'email', 'phone_number',
                                              'license_ID', 'license_category', 'create_at')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response
