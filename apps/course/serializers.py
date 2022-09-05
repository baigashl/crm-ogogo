from .models import Course
from rest_framework import serializers
from rest_framework.reverse import reverse
from apps.mentor.serializers import MentorSerializer
from apps.students.serializers import StudentSerializer
from apps.students.models import Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'mentor', 'name', 'description', 'address', 'start_date', 'active', 'course_type']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)

    # def get_students(self, obj):
    #     data = Student.objects.filter(course_id=obj.id)
    #     return StudentSerializer(data, many=True).data


class CourseDetailSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer(read_only=True)
    students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'mentor', 'name', 'description', 'students', 'address', 'start_date', 'course_type']

    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     return reverse("detail", kwargs={'id': obj.id}, request=request)

    def get_students(self, obj):
        data = Student.objects.filter(course_id=obj.id)
        return StudentSerializer(data, many=True).data
