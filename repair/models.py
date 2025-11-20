from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from embed_video.fields import EmbedVideoField
from django.utils.safestring import mark_safe
from django.utils.crypto import get_random_string




# Create your models here.
class Repairs(models.Model):


    vehicle = models.CharField(blank=True, max_length=50)
    fullname = models.CharField(blank=True, max_length=50)
    report_date = models.DateTimeField(blank=True)
    mileage = models.FloatField()
    issue = RichTextUploadingField(blank=True)
    registration_plate = models.CharField(blank=True, max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Repairs'



class RepairForm(ModelForm):
    class Meta:
        model = Repairs
        fields = ['vehicle', 'fullname', 'report_date', 'mileage', 'issue', 'registration_plate',]


