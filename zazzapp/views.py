from rest_framework import generics
from zazzapp.models import Shout
from zazzapp.seralizers import ShoutSeralizer


class Shout(generics.ListCreateAPIView):
    queryset = Shout.objects.all()
    serializer_class = ShoutSeralizer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
