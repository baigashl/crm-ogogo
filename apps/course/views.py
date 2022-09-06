from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Course
from apps.students.models import Student
from .serializers import CourseSerializer, CourseDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from apps.students.models import Student
from rest_framework.parsers import JSONParser

from ..students.serializers import StudentSerializer


class CourseListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    parser_classes = [JSONParser]

    def get(self, request):
        snippets = Course.objects.filter(active=True)
        data_list = []
        for c in snippets:
            serializer = CourseSerializer(c)
            data = serializer.data
            serializer2 = StudentSerializer(Student.objects.filter(course_id=c.id), many=True)
            data['student_count'] = len(serializer2.data)
            data_list.append(data)
        return Response(data_list)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        students = Student.objects.filter(course=id)
        serializer = CourseDetailSerializer(snippet)
        serializer2 = StudentSerializer(students, many=True)
        data = serializer.data
        data['students'] = serializer2.data
        data['students_count'] = len(serializer2.data)
        return Response(data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CourseDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseUpdateAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CourseSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseMoveToArchiveAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        snippet = Course.objects.get(id=id)
        snippet.active = False
        snippet.save()
        print(snippet.active)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchiveCourseListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request):
        snippets = Course.objects.filter(active=False)
        serializer = CourseSerializer(snippets, many=True)
        return Response(serializer.data)


class CourseDeleteAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
