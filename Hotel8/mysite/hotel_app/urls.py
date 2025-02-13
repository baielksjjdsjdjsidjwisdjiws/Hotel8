from .views import *
from django.urls import path, include
from rest_framework import routers


router =routers.SimpleRouter()




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
    path('room/', RoomCreateAPIView.as_view(), name='room_create'),
    path('booking/', BookingCreateAPIView.as_view(), name='booking_create'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),]