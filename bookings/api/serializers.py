from rest_framework import serializers

from bookings.models import Room, RoomImage, Booking


class RoomImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = RoomImage
        exclude = ("room",)


class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
