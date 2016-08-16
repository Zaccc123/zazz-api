from rest_framework import serializers
from zazzapp.models import Shout


class ShoutSeralizer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Shout
        fields = ('id', 'message', 'username', 'created_at')
