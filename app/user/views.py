"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Ceate a new user in the view"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authentioncated user."""
    serializer_class = UserSerializer
    authentication_class = [authentication.TokenAuthentication]
    permissions_class = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
