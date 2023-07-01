from django.contrib import admin
from .models import Country, GalleryCollection, Gallery, ContinentGallery, Region

# Register your models here.

@admin.register(GalleryCollection)
class GalleryCollectionAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['category', 'image']


admin.site.register(Country)
admin.site.register(ContinentGallery)
admin.site.register(Region)