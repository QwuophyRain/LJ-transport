from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.core.paginator import Paginator
from .filters import BookingFilter, BusFilter
from .models import *
from vehicle.models import Vehicles
import json
import os
from account.models import UserProfile
from home.models import *
from .models import *
import datetime
from datetime import datetime
import xlwt




# Create your views here.
def index(request):
    return HttpResponse("booking")

@login_required(login_url='/login')
def makeBookings(request):
    setting = Settings.objects.get(pk=1)
    list = Vehicles.objects.all().order_by('?')
    context = {'setting': setting, 'list': list,}
    # filter
    filtered_bus = BusFilter(
        request.GET,
        queryset=Vehicles.objects.all().order_by('-id')
    )
    count = filtered_bus.qs.count()

    context['filtered_room'] = filtered_bus
    context['count'] = count

    # pagination
    paginated_bus = Paginator(filtered_bus.qs, 6)
    page_number = request.GET.get('page')
    bus_page_obj = paginated_bus.get_page(page_number)

    context['bus_page_obj'] = bus_page_obj

    return render(request, 'make_bookings.html', context=context)


@login_required(login_url='/login')
def bookThis(request, id):
    current_user = request.user
    count_orders = OrderBus.objects.filter(user_id=current_user.id).count()
    setting = Settings.objects.get(pk=1)
    viewBuses = Vehicles.objects.get(pk=id)
    list = Vehicles.objects.all().order_by('?')
    context = {'setting': setting,  'list': list, 'viewBuses': viewBuses,
                'count_orders': count_orders}
    return render(request, 'book_this.html', context)



@login_required(login_url='/login')
def addtobuscart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user
    checkbus = Booking.objects.filter(bus_id=id)

    if checkbus:
        control = 1
    else:
        control = 0

    if request.method == 'POST':  # check post
        form = BookForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = Booking.objects.get(bus_id=id)  # create relation with mode
                data.pickup = form.cleaned_data['pickup']
                data.start_date = form.cleaned_data['start_date']
                data.end_date = form.cleaned_data['end_date']
                data.security_deposit = form.cleaned_data['security_deposit']
                data.save()  # save data to table

            else:
                data = Booking()
                data.user_id = current_user.id
                data.bus_id = id
                data.pickup = form.cleaned_data['pickup']
                data.start_date = form.cleaned_data['start_date']
                data.end_date = form.cleaned_data['end_date']
                data.security_deposit = form.cleaned_data['security_deposit']
                data.save()
        messages.success(request, f'You have successfully booked our {data.bus} at GHC{data.bus.cost_per_day} per day. '
                                   f'You will start on {data.start_date} and end  on {data.end_date}.'
                                   f' You are therefore using the bus for a period of  {data.diff} days at a cost of GHC{data.amount}. Thank you!')
        # return HttpResponseRedirect(url)  # redirect to contact page after submitting message
        return HttpResponseRedirect('/booking_list')  # redirect to contact page after submitting message

    else:

        if control == 1:
            data = Booking.objects.get(bus_id=id)
            data.children = ['pickup']
            data.adult = ['start_date']
            data.check_in = ['end_date']
            data.check_out = ['security_deposit']
            data.save()
        else:
            data = Booking()
            data.user_id = current_user.id
            data.bus_id = id
            data.children = ['pickup']
            data.adult = ['start_date']
            data.check_in = ['end_date']
            data.check_out = ['security_deposit']
            data.save()
        messages.success(request,  f'You have successfully booked our {data.bus} at GHC{data.vehicles.cost_per_day} per day. '
                                   f'You will start on {data.start_date} and end  on {data.end_date}.'
                                   f' You are therefore using the bus for a period of  {data.diff} days at a cost of GHC{data.amount}. Thank you!')
        return HttpResponseRedirect(url)  # redirect to contact page after submitting message



@login_required(login_url='/login')   # shopping for only members
def bookedCart(request):
    setting = Settings.objects.get(pk=1)
    current_user = request.user
    booking = Booking.objects.filter(user_id=current_user.id)
    count_orders = OrderBus.objects.filter(user_id=current_user.id).count()
    list = Vehicles.objects.all().order_by('?')
    total = 0
    for rs in booking:
        total += rs.amount

    context = {'booking': booking, 'setting': setting, 'total': total,
               'list': list, 'count_orders': count_orders}
    return render(request, 'booking_list.html', context)


@login_required(login_url='/login')   # shopping for only members
def deletefromcart(request, id):
    Booking.objects.filter(id=id).delete()
    messages.success(request, "Bus sucessfully Deleted!")
    return HttpResponseRedirect("/booked_details")



@login_required(login_url='/login')   # shopping for only members
def orderbus(request):
    current_user = request.user
    booking = Booking.objects.filter(user_id=current_user.id)
    setting = Settings.objects.get(pk=1)
    count_orders = OrderBus.objects.all().count()

    total = 0
    for rs in booking:
        total += rs.amount

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            # You can add credit card infor here
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            booking = Booking.objects.filter(user_id=current_user.id)
            for rs in booking:
                detail = OrderBus()
                detail.order_id = data.id
                detail.bus_id = rs.bus_id
                detail.user_id = current_user.id
                detail.amount = rs.amount
                detail.save()

                bus = Vehicles.objects.get(id=rs.bus_id)
                # room.amount -= rs.quantity
                bus.save()

            Booking.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your order has been completed. Write down your order code for references. Thank You!")
            return render(request, 'order_completed.html', {'ordercode': ordercode, 'setting': setting,
                                                            'count_orders': count_orders})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("booking/orderbus")

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    count_orders = OrderBus.objects.filter(user_id=current_user.id).count()
    context = {'booking': booking, 'total': total, 'setting': setting,  'form': form,
               'profile': profile, 'count_orders': count_orders}
    return render(request, 'order_form.html', context)



@login_required(login_url='/login')   # shopping for only members
def ordered_buses(request):
    setting = Settings.objects.get(pk=1)
    current_user = request.user
    booking = Booking.objects.filter(user_id=current_user.id)
    count_orders = OrderBus.objects.filter(user_id=current_user.id).count()
    ordered = OrderBus.objects.filter(user_id=current_user.id).order_by('-id')
    list = Vehicles.objects.all().order_by('?')


    context = {'ordered': ordered, 'setting': setting,
               'list': list, 'count_orders': count_orders, 'booking': booking}
    return render(request, 'my_ordered_buses.html', context)


def exportBookings(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Bookings' +\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Bookings Data') # this will make a sheet named Assignment Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Vehicle', 'Pick Up', 'Destination', 'Start Date', 'End Date', 'Deposit', 'Cost', 'Booked By', 'Phone', 'Driver', 'Booked On' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Booking.objects.all().values_list('vehicle', 'source', 'destination', 'start_date', 'end_date', 'security_deposit',
                                              'cost', 'booker', 'booker_phone', 'assigned_driver', 'booked_on')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response
