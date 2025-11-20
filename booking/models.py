from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from PIL import Image
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from vehicle.models import Vehicles


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bus = models.ForeignKey(Vehicles, on_delete=models.SET_NULL, null=True)
    pickup = models.CharField(blank=True, max_length=100)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    security_deposit = models.FloatField(default=0, blank=True)
    cost = models.FloatField(default=0, blank=True)
    assigned_driver = models.CharField(blank=True, max_length=100)
    notes = RichTextUploadingField(blank=True)
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Booking ID: " + str(self.id)

    @property
    def diff(self):
        diff = self.end_date - self.start_date
        return diff.days


    @property
    def amount(self):
        return (self.bus.cost_per_day * self.diff)


class BookForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup', 'start_date', 'end_date', 'security_deposit']


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=150, blank=True)
    total = models.FloatField()
    status = models.CharField(max_length=30, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone']


class OrderBus(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Cancelled', 'Cancelled'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=30, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle.bus_name