from rest_framework import generics

from .serializers import RoomSerializer, BookingSerializer
from bookings.models import Room, Booking


class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_url_kwarg = 'room_id'


class BookedDatesOfRoomListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer
    lookup_url_kwarg = 'room_id'

    def get_queryset(self):
        return Booking.objects.filter(room_id=self.kwargs['room_id'])
