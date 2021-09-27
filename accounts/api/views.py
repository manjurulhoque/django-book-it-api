from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserCreateSerializer, UserSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user_serializer = UserSerializer(serializer.instance)

        return Response(user_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
