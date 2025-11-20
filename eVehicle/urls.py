"""
URL configuration for eVehicle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from home import views
from account import views as AccountViews
from vehicle import views as VehicleViews
from repair import views as RepairViews
from driver import views as DriverViews
from booking import views as BookingViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('account/', include('account.urls')),
    path('vehicle/', include('vehicle.urls')),
    path('driver/', include('driver.urls')),
    path('repair/', include('repair.urls')),
    path('booking/', include('booking.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),



    # Users urls
    path('register/', AccountViews.register, name='register'),
    path('profile/', AccountViews.profile, name='profile'),
    path('profile_update/', AccountViews.profileUpdate, name='profile_update'),
    path('login/', AccountViews.loginform, name='login'),
    path('login2/', auth_views.LoginView.as_view(template_name='login2.html'), name='login2'),

    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('logout2/', AccountViews.logoutfunc, name='logoutfunc'),

    path('logout/', AccountViews.logout_request, name="logout"),

    # driver urls
    path('new_driver/', DriverViews.addDriver, name='new_driver'),
    path('driver_list/', DriverViews.driverList, name='driver_list'),
    path('update_driver/<int:pk>/', DriverViews.updateDrivers, name='update_driver'),
    path('delete_driver/<str:pk>/', DriverViews.delete_driver, name="delete_driver"),
    path('export/excel', DriverViews.exportDrivers, name='export_excel'),

    # vehicle urls
    path('new_vehicle/', VehicleViews.addVehicles, name='new_vehicle'),
    path('vehicle_list/', VehicleViews.vehicleList, name='vehicle_list'),
    path('update_vehicle/<int:pk>/', VehicleViews.updateVehicles, name='update_vehicle'),
    path('delete_vehicle/<str:pk>/', VehicleViews.delete_vehicle, name="delete_vehicle"),


    # booking urls
    path('make_bookings/', BookingViews.makeBookings, name='make_bookings'),
    # path('booking_list/', BookingViews.bookingList, name='booking_list'),
    # path('update_booking/<int:pk>/', BookingViews.updateBooking, name='update_booking'),
    # path('delete_booking/<str:pk>/', BookingViews.deleteBooking, name="delete_booking"),
    path('export/excel', BookingViews.exportBookings, name='export_excel'),

    path('book_this/<int:id>', BookingViews.bookThis, name='book_this'),
    # path('bus_details/<int:id>', BookingViews.aboutbus, name='bus_details'),
    path('booking_list/', BookingViews.bookedCart, name='booking_list'),
    path('my_ordered_buses/', BookingViews.ordered_buses, name='my_ordered_buses'),


    # Repairs urls
    path('add_repair/', RepairViews.addRepair, name='add_repair'),
    path('repair_list/', RepairViews.repairList, name='repair_list'),
    path('update_repairs/<int:pk>/', RepairViews.updateRepair, name='update_repairs'),
    path('delete_repair/<str:pk>/', RepairViews.deleteRepair, name="delete_repair"),
    path('export/excel', RepairViews.exportRepairs, name='export_excel'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


