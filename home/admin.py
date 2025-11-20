from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

# Register your models here.
class SettingAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'logo']


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'update_at']
    # you can only read these fields and not alter them since they're from your client
    readonly_fields = ['name', 'email', 'phone', 'message']
    list_filter = ['status', 'create_at', 'update_at']


admin.site.register(Settings, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
