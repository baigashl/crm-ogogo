from .models import Student
from rest_framework import serializers
from rest_framework.reverse import reverse


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'course', 'first_name', 'second_name', 'phone', 'paid', 'description', 'quantity_of_classes']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)
