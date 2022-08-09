from .models import Mentor
from rest_framework import serializers
from rest_framework.reverse import reverse


class MentorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentor
        fields = ['id', 'name', 'second_name', 'phone', 'quantiy_of_classes']

    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     return reverse("detail", kwargs={'id': obj.id}, request=request)
