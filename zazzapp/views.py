from rest_framework import generics, permissions
from zazzapp.models import Shout
from zazzapp.seralizers import ShoutSeralizer, UserSerializer
from django.contrib.auth.models import User


class User(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class Shout(generics.ListCreateAPIView):
    queryset = Shout.objects.all()
    serializer_class = ShoutSeralizer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
