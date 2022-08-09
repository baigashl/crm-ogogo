from .models import ClassQuantity
from rest_framework import serializers


class ClassQuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassQuantity
        fields = ['id', 'mentor', 'date', 'quantity_of_classes']
