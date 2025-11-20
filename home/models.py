from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from embed_video.fields import EmbedVideoField
from django.utils.safestring import mark_safe
from django.utils.crypto import get_random_string



# Create your models here.
class Settings(models.Model):

    title = models.CharField(max_length=150)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=100)
    mobile = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    logo = models.ImageField(blank=True, upload_to='image/')
    motto = models.CharField(blank=True, max_length=150)
    vision = models.CharField(blank=True, max_length=300)
    mission = models.CharField(blank=True, max_length=300)
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    telegram = models.CharField(blank=True, max_length=50)
    linkedIn = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    whatsapp = models.CharField(blank=True, max_length=50)
    about = RichTextUploadingField(blank=True)
    about_video = EmbedVideoField(blank=True)
    sample_about = RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Settings'


class ContactMessage(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read'),
    )

    name = models.CharField(blank=True, max_length=100)
    email = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=30)
    subject = models.CharField(blank=True, max_length=100)
    message = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')
    note = models.CharField(blank=True, max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact Messages'



class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message', 'subject']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Your Fullname'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message'}),
        }
