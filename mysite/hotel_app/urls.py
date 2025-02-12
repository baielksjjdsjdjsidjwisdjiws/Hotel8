from .views import *
from django.urls import path, include
from rest_framework import routers


router =routers.SimpleRouter()
router.register(r'room', RoomViewSet, basename='room_list')
router.register(r'booking', BookingViewSet, basename='booking_list')



urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileEditAPIView.as_view(), name='user_edit'),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('rating/', RatingListAPIView.as_view(), name='rating_list'),
    path('rating/<int:pk>/', RatingCreateAPIView.as_view(), name='rating_create'),
]