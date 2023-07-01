from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.


def startPage(request):
    countries = Country.objects.all()
    context = {'countries' : countries}
    return render(request, 'baseapp/startPage.html', context)


def aboutPage(request):
    context = {}
    return render(request, 'baseapp/aboutPage.html', context)


def contactPage(request):
    context = {}
    return render(request, 'baseapp/contactPage.html', context)


def galleryPage(request):

    context = {}
    return render(request, 'baseapp/galleryPage.html', context)


def countriesPage(request):
    countries = Country.objects.all()
    context = {'countries' : countries}
    return render(request, 'baseapp/countriesPage.html', context)


def mapPage(request, id):
    country = Country.objects.get(pk=id)
    context = {'country' : country}
    return render(request, 'baseapp/mapPage.html', context)


def countryAbout(request, id):
    country = Country.objects.get(pk=id)
    context = {'country' : country}
    return render(request, 'baseapp/countryAbout.html', context)


def regionAbout(request):
    regions = Region.objects.all()
    context = {'regions' : regions}
    return render(request, 'baseapp/regionAbout.html', context)
