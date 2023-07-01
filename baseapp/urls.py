from django.urls import path
from . import views

urlpatterns = [
    path('', views.startPage, name='start'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),
    path('gallery/', views.galleryPage, name='gallery'),
    path('countries/', views.countriesPage, name='countries'),
    path('map/<int:id>/', views.mapPage, name='map'),
    path('countryAbout/<int:id>/', views.countryAbout, name='about'),
    path('regionAbout/', views.regionAbout, name='region'),
]

