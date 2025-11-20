import django_filters
from .models import Repairs




class RepairFilter(django_filters.FilterSet):

    class Meta:
        model = Repairs
        fields = [

            # 'booker',
            'registration_plate',

        ]


