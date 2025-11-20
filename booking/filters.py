import django_filters
from .models import Booking
from vehicle.models import Vehicles




class BookingFilter(django_filters.FilterSet):

    class Meta:
        model = Booking
        fields = [

            # 'booker',
            'bus',

        ]


class BusFilter(django_filters.FilterSet):

    class Meta:
        model = Vehicles
        fields = [
            'bus_name',

        ]