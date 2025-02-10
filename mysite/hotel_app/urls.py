from .views import *
from django.urls import path, include
from rest_framework import routers


router =routers.SimpleRouter()
router.register(r'profile', UserProfileViewSet, basename='profile_list')
router.register(r'city', CityViewSet, basename='city_list')
router.register(r'room', RoomViewSet, basename='room_list')
router.register(r'booking', BookingViewSet, basename='booking_list')
router.register(r'hotel', HotelViewSet, basename='hotel_list')
router.register(r'review', RatingViewSet, basename='review_list')


urlpatterns = [
    path('', include(router.urls)),
]