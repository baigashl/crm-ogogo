from .models import ClassQuantity, StudentClassQuantity
from rest_framework import serializers


class ClassQuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassQuantity
        fields = ['id', 'mentor', 'date', 'quantity_of_classes']


class StudentClassQuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentClassQuantity
        fields = ['id', 'student', 'course', 'date', 'quantity_of_classes']
