"""
Views for the user API.
"""
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Ceate a new user in the view"""
    serializer_class = UserSerializer
