from rest_framework.generics import ListAPIView

from .serializers import RoomSerializer
from bookings.models import Room


class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
