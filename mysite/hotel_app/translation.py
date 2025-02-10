from .models import City, Hotel
from modeltranslation.translator import TranslationOptions,register

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name', )


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'description')



