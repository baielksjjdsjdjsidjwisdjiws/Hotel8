from .models import *
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
