from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

# Create your views here.


def startPage(request):
    # if request.method == 'POST':
    #     images = request.FILES.getlist('images')
    #     for image in images:
    #         newImage = Gallery(image=image)
    #         newImage.save()

    countries = Country.objects.all()
    regions = Region.objects.all()
    galleries = Gallery.objects.all()

    #Pagination

    context = {'countries' : countries, 'regions' : regions, 'galleries' : galleries}
    return render(request, 'baseapp/startPage.html', context)



def aboutPage(request):
    countries = Country.objects.all()
    regions = Region.objects.all()
    context = {'countries' : countries, 'regions' : regions}
    return render(request, 'baseapp/aboutPage.html', context)


def contactPage(request):
    countries = Country.objects.all()
    regions = Region.objects.all()
    context = {'countries' : countries, 'regions' : regions}
    return render(request, 'baseapp/contactPage.html', context)


def galleryPage(request):
    countries = Country.objects.all()
    regions = Region.objects.all()
    context = {'countries' : countries, 'regions' : regions}

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
