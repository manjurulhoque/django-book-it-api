from rest_framework import serializers

from bookings.models import Room, RoomImage


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        exclude = ("room",)


class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"
