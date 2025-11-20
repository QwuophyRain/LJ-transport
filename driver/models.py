from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea, FileInput
from embed_video.fields import EmbedVideoField
from django.utils.safestring import mark_safe
from django.utils.crypto import get_random_string



# Create your models here.
class Drivers(models.Model):
    CATEGORY = (
        ('AM', 'AM'),
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A', 'A'),
        ('B', 'B'),
        ('BE', 'BE'),
        ('W', 'W'),
        ('C', 'C'),
        ('CE', 'CE'),
        ('C1', 'C1'),
        ('C1E', 'C1E'),
        ('D', 'D'),
        ('DE', 'DE'),
        ('D1', 'D1'),
        ('D1E', 'D1E'),
    )


    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    national_id = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=150)
    email = models.CharField(blank=True, max_length=50)
    phone_number = models.CharField(blank=True, max_length=50)
    license_ID = models.CharField(blank=True, max_length=20)
    license_category = models.CharField(max_length=15, choices=CATEGORY, default='category')
    photo = models.ImageField(blank=True, upload_to='image/drivers', default='user.png',)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Drivers'



class DriverForm(ModelForm):
    class Meta:
        model = Drivers
        fields = ['first_name', 'last_name', 'national_id', 'address', 'email', 'phone_number',
                  'license_ID', 'license_category', 'photo']
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'national_id': TextInput(attrs={'class': 'input', 'placeholder': 'National ID'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'phone_number': TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'license_ID': TextInput(attrs={'class': 'input', 'placeholder': 'Licensed ID'}),
            'license_category': TextInput(attrs={'class': 'input', 'placeholder': 'Licensed ID'}),
            'photo': FileInput(attrs={'style': 'display: none;', 'class': 'form-control', 'required': False}),


        }

