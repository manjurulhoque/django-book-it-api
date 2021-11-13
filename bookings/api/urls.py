from django.urls import path

from . import views

urlpatterns = [
    path('rooms', views.RoomListAPIView.as_view()),
    path('rooms/<int:room_id>', views.RoomDetailsAPIView.as_view()),
    path('bookings/<int:room_id>/booked-dates', views.BookedDatesOfRoomListAPIView.as_view()),
]
