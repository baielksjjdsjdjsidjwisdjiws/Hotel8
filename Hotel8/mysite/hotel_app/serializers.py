from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', 'date_registered')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }




class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name']


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']



class RoomListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id']


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'



class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user' , 'booking_hotel',
                  'departure', 'check_in', 'adults', 'children', 'room', 'created_date']



class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y'))
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Rating
        fields = ['user', 'text', 'parent', 'stars', 'created_date']


class RatingSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'stars', 'text']



class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'



class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'


class HotelListSerializers(serializers.ModelSerializer):
    city = CitySerializers()
    hotel_images = HotelImageSerializers(many=True, read_only=True)
    hotel_stars = RatingSimpleSerializer(read_only=True, many=True)
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_images', 'hotel_status', 'city', 'hotel_stars']



class CityDetailSerializers(serializers.ModelSerializer):
    city_names = HotelListSerializers

    class Meta:
        model = City
        fields = ['city_name', 'city_names']

class RoomDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_num', 'status']


class HotelDetailSerializers(serializers.ModelSerializer):
    city = CitySerializers()
    hotel_stars = RatingSerializer(many=True, read_only=True)
    hotel_images = HotelImageSerializers(many=True, read_only=True)
    room = RoomSerializers(read_only=True)
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_images', 'hotel_status', 'city', 'hotel_stars', 'room']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_user(self, obj):
        return obj.get_count_user()