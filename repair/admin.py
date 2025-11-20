from django.contrib import admin
from.models import Repairs

# Register your models here.

class RepairAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'vehicle']
    list_filter = ['fullname']

admin.site.register(Repairs, RepairAdmin)
