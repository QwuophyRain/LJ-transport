from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .models import Repairs, RepairForm
from home.models import Settings
from .filters import RepairFilter
from django.core.paginator import Paginator
from datetime import datetime
import datetime
import xlwt
import json




# Create your views here.
def index(request):
    return HttpResponse("driver")


def addRepair(request):
    if request.method == 'POST':  # check post
        form = RepairForm(request.POST)
        if form.is_valid():
            data = Repairs()  # create relation with mode
            data.vehicle = form.cleaned_data['vehicle']
            data.fullname = form.cleaned_data['fullname']
            data.report_date = form.cleaned_data['report_date']
            data.mileage = form.cleaned_data['mileage']
            data.issue = form.cleaned_data['issue']
            data.registration_plate = form.cleaned_data['registration_plate']
            data.save()  # save data to table
            messages.success(request, "Report Successfully Added. Thank you..")  # flash message
            return HttpResponseRedirect('/repair_list')  # redirect to home page after submitting comment

        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/')

    setting = Settings.objects.get(pk=1)
    repairs = Repairs.objects.all().order_by('?')[:6]
    context = {'setting': setting, 'repairs': repairs}
    return render(request, 'add_repair.html', context)


def repairList(request):
    setting = Settings.objects.get(pk=1)
    repairs = Repairs.objects.all().order_by('-id')[:9]

    context = {'setting': setting, 'repairs': repairs}

    # filter
    filtered_repair = RepairFilter(
        request.GET,
        queryset=Repairs.objects.all().order_by('-id')
    )
    count = filtered_repair.qs.count()

    context['filtered_repair'] = filtered_repair
    context['count'] = count

    # pagination
    paginated_repair = Paginator(filtered_repair.qs, 6)
    page_number = request.GET.get('page')
    repair_page_obj = paginated_repair.get_page(page_number)

    context['repair_page_obj'] = repair_page_obj

    return render(request, 'repair_list.html', context=context)


@login_required(login_url='/login')
def deleteRepair(request, pk):
    repairs = Repairs.objects.get(id=pk)
    if request.method == 'POST':
        repairs.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/repair_list')
    return render(request, 'delete_repair.html')


@login_required(login_url='/login')
def updateRepair(request, pk):
    repairs = Repairs.objects.get(id=pk)

    if request.method == 'POST':

        repairs.vehicle = request.POST.get('vehicle')
        repairs.fullname = request.POST.get('fullname')
        repairs.report_date = request.POST.get('report_date')
        repairs.mileage = request.POST.get('mileage')
        repairs.issue = request.POST.get('issue')
        repairs.registration_plate = request.POST.get('registration_plate')
        repairs.save()
        messages.success(request, 'Successfully Updated')
        return redirect('/repair_list')

    setting = Settings.objects.get(pk=1)

    context = {
        'repairs': repairs, 'setting': setting,
    }
    return render(request, 'update_repairs.html', context)



def exportRepairs(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Repairs' +\
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Repairs Data') # this will make a sheet named drivers data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Vehicle Name', 'Registration Plate', 'Mileage',  'Reported Issue',  'Reported By', 'Reported Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Repairs.objects.all().values_list('vehicle', 'registration_plate', 'mileage', 'issue', 'fullname', 'reported_date',
                                              'license_ID', 'license_category', 'create_at')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response