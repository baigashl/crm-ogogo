from .models import Student
from rest_framework import serializers
from rest_framework.reverse import reverse


class StudentSerializer(serializers.ModelSerializer):
    paid = serializers.SerializerMethodField('get_paid')

    class Meta:
        model = Student
        fields = ['id',
                  'course',
                  'email',
                  'first_name',
                  'second_name',
                  'phone',
                  'paid',
                  'first_month_paid',
                  'second_month_paid',
                  'third_month_paid',
                  'fourth_month_paid',
                  'description',
                  'active',
                  'qr_code'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)

    def get_paid(self, obj):
        all_paid = obj.first_month_paid + obj.second_month_paid + obj.third_month_paid + obj.fourth_month_paid
        return all_paid


class StudentDetailSerializer(serializers.ModelSerializer):
    paid = serializers.SerializerMethodField('get_paid')

    class Meta:
        model = Student
        fields = ['id',
                  'course',
                  'email',
                  'first_name',
                  'second_name',
                  'phone',
                  'paid',
                  'first_month_paid',
                  'second_month_paid',
                  'third_month_paid',
                  'fourth_month_paid',
                  'description',
                  'active',
                  'qr_code'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)

    def get_paid(self, obj):
        all_paid = obj.first_month_paid + obj.second_month_paid + obj.third_month_paid + obj.fourth_month_paid
        return all_paid
