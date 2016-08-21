from rest_framework import serializers
from zazzapp.models import Shout
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)
        write_only_fields = ('password')


class ShoutSeralizer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Shout
        fields = ('id', 'message', 'username', 'created_at')
        read_only_fields = ('id',)
