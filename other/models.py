from django.db import models
from .utils import rasm_olchami, image_size, logo_size
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blog _images', validators=[rasm_olchami])
    des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.title
    

class Reklama(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blog _images', validators=[image_size])
    link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.title

 

class MySettings(models.Model):
    name = models.CharField(max_length=40, verbose_name="Name", null=True, blank=True)
    facebook = models.URLField(max_length=40, verbose_name="Facebook", null=True, blank=True)
    telegram = models.URLField(max_length=40, verbose_name="Telegram", null=True, blank=True)
    youtube = models.URLField(max_length=40, verbose_name="Youtube", null=True, blank=True)
    instagram = models.URLField(max_length=40, verbose_name="Instagram", null=True, blank=True)
    logo = models.ImageField(upload_to="logo/", validators=[logo_size], verbose_name="Logo", null=True, blank=True)
    location = models.URLField(max_length=300, verbose_name="Location", null=True, blank=True)
    locationiframe = models.URLField(max_length=400, verbose_name="Location for Contact", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number", null=True, blank=True)
    email = models.CharField(max_length=20, verbose_name="Email", null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name="Title", null=True, blank=True)
    address = models.CharField(max_length=300, verbose_name="Address", null=True, blank=True)
    about_us = RichTextField(verbose_name="About Us", null=True, blank=True)
    about_us_image = models.ImageField(upload_to="images/", verbose_name="About Us Image", null=True, blank=True)


    @property
    def about_imageURL(self):
        try:
            return self.about_us_image.url
        except:
            return ''
        
    @property
    def logoURL(self):
        try:
            return self.logo.url
        except:
            return ''

    def __str__(self):
        return self.title


class Team(models.Model):
    fio = models.CharField(max_length=50)
    job = models.CharField(max_length=70)
    image = models.ImageField(upload_to="team_image")

    facebook = models.CharField(max_length=40, verbose_name="Facebook", null=True, blank=True)
    telegram = models.CharField(max_length=40, verbose_name="Telegram", null=True, blank=True)
    instagram = models.CharField(max_length=40, verbose_name="Instagram", null=True, blank=True)  

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.fio