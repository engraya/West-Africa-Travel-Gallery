from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=200, null=True, blank=True)
    dialingCode = models.CharField(max_length=200, null=True, blank=True)
    currency = models.CharField(max_length=200, null=True, blank=True)
    population = models.CharField(max_length=200, null=True, blank=True)
    officialLanguage = models.CharField(max_length=200, null=True, blank=True)
    mapImage = models.ImageField(upload_to='images', max_length=100, null=True, blank=True)
    coverPhoto1 = models.ImageField(upload_to='images', max_length=100, null=True, blank=True)
    coverPhoto2 = models.ImageField(upload_to='images', max_length=100, null=True, blank=True)
    coverPhoto3 = models.ImageField(upload_to='images', max_length=100, null=True, blank=True)
    countryFlag = models.ImageField(upload_to='images', max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    climate =  models.TextField(null=True, blank=True)
    culture = models.TextField(null=True, blank=True)
    wikiLink = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class GalleryCollection(models.Model):

    COUNTRY_CHOICES = (
        ("Nigeria", "Nigeria"),
        ("Niger", "Niger"),
        ("Ghana", "Ghana"),
        ("Gambia", "Gambia"),
        ("Sierra Leone", "Sierra Leone"),
        ("Togo", "Togo"),
        ("Benin Republic", "Benin Republic"),
        ("Mali", "Mali"),
        ("Senegal", "Senegal"),
        ("Guinea", "Guinea"),
        ("Mauritania", "Mauritania"),
        ("Ivory Coast", "Ivory Coast"),
        ("Liberia", "Liberia"),
        ("Guinea Bissau", "Guinea Bissau"),
        ("Burkina Faso", "Burkina Faso"),
    )
    image =  models.ImageField(upload_to='images', max_length=100, null=True, blank=True)
    category = models.CharField(max_length=20, choices=COUNTRY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.id



class Gallery(models.Model):
    title = models.CharField(max_length=255, default='', null=True, blank=True)
    category = models.ForeignKey(Country, null=True, blank=True, on_delete=models.PROTECT)
    image =  models.ImageField(upload_to='images', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Region(models.Model):
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=200, null=True, blank=True)
    timezone = models.CharField(max_length=200, null=True, blank=True)
    population = models.CharField(max_length=200, null=True, blank=True)
    mapImage = models.ImageField(upload_to='images', max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    climate =  models.TextField(null=True, blank=True)
    culture = models.TextField(null=True, blank=True)
    wikiLink = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    density = models.CharField(null=True, blank=True, max_length=200)
    gdp = models.CharField(null=True, blank=True, max_length=200)
    beliefs = models.TextField(null=True, blank=True)
    goods = models.TextField(null=True, blank=True)
    flavours = models.TextField(null=True, blank=True)
    countries = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name




class ContinentGallery(models.Model):
    image =  models.ImageField(upload_to='images/westAfrica', max_length=100, null=True, blank=True)
   


