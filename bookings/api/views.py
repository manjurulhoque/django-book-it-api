from rest_framework import generics

from .serializers import RoomSerializer
from bookings.models import Room


class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_url_kwarg = 'room_id'
