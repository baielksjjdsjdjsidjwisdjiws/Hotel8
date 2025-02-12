from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import IntegerField
from phonenumber_field.formfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(55)], null=True, blank=True)
    phone_number = PhoneNumberField()
    PROFILE_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner')
    )
    profile = models.CharField(max_length=16, choices=PROFILE_CHOICES, default='client')
    country = models.CharField(max_length=34)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'



class City(models.Model):
    city_name = models.CharField(max_length=34, unique=True)

    def __str__(self):
        return self.city_name



class Room(models.Model):
    room_num = IntegerField(choices=[(i, str(i)) for i in range(1, 51)])
    STATUS_CHOICES = (
        ('free', 'free'),
        ('booked', 'booked'),
        ('busy', 'busy')
    )
    status = models.CharField(max_length=34, choices=STATUS_CHOICES, default='free')
    TYPE_CHOICES = (
        ('1room', '1room'),
        ('2room', '2room'),
        ('domestic', 'domestic'),
    )
    type = models.CharField(max_length=34, choices=TYPE_CHOICES, default='1room')
    description = models.TextField()

    def __str__(self):
        return f'{self.status}, {self.type}'



# class Booking(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
#     data = models.DateField()
#     room = models.ManyToManyField(Room)
#     def __str__(self):
#         return f'{self.user}, {self.room}'


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=34)
    hotel_status = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)])
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_names')
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_hotel', null=True, blank=True)


    def __str__(self):
        return self.hotel_name

    def get_avg_rating(self):
        all_ratings = self.hotel_stars.all()
        if all_ratings.exists():
            return round(sum([i.stars for i in all_ratings]) / all_ratings.count(), 1)
        return 0

    def get_count_user(self):
        return self.hotel_stars.count()




class RoomImage(models.Model):
    room_images = models.ImageField(upload_to='room_images')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_hot_im', null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_room_ig', null=True, blank=True)


class HotelImage(models.Model):
    hotel_image = models.ImageField(upload_to='hotel_images')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='hotel_user')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_stars')
    stars = models.IntegerField(choices=[(i, str(i))for i in range(1,11)], null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'



class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    booking_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='booking')
    check_in=models.DateTimeField()
    departure = models.DateTimeField()
    adults =models.PositiveSmallIntegerField(default=1)
    children = models.PositiveSmallIntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.room}'