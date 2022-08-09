from .models import Administrator
from rest_framework import serializers


class AdministratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Administrator
        fields = ['id', 'email', 'name', 'second_name', 'branch']
