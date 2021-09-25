from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.FloatField()
    address = models.CharField(max_length=255)
    guest_capacity = models.IntegerField()
    beds = models.IntegerField()
    internet = models.BooleanField()
    breakfast = models.BooleanField()
    air_conditioned = models.BooleanField()
    pets_allowed = models.BooleanField()
    room_cleaning = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="rooms")

    def __str__(self):
        return self.room.name
