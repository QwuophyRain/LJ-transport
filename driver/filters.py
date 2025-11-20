import django_filters
from .models import Drivers




class DriverFilter(django_filters.FilterSet):

    class Meta:
        model = Drivers
        fields = [


            'license_ID',

        ]


