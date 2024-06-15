# serializers.py
from rest_framework import serializers
from .models import HostRequest, Host

class HostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostRequest
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class AdminActionSerializer(serializers.Serializer):
    request_id = serializers.IntegerField()
    action = serializers.ChoiceField(choices=['accept', 'reject'])