from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin



class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1


@admin.register(City)
class CityAdmin(TranslationAdmin):


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Hotel)
class HotelAdmin(CityAdmin):
   inlines = [HotelImageInline]




admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(Room)
admin.site.register(Booking)

