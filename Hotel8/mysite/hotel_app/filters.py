from django_filters import FilterSet
from .models import Hotel

class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'city': ['exact'],
            'hotel_name': ['exact'],
        }