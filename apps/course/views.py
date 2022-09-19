from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Course, CourseType
from apps.students.models import Student
from .serializers import CourseSerializer, CourseDetailSerializer, CourseTypeSerializer, CountSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from apps.students.models import Student
from rest_framework.parsers import JSONParser
from apps.administrator.permissions import IsSubAdminPermission

from ..students.serializers import StudentSerializer
from django.core.paginator import Paginator


class CourseListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    parser_classes = [JSONParser]

    def get(self, request):
        snippets = Course.objects.filter(active=True)
        data_list = []
        page_num = int(self.request.query_params.get('page'))
        for c in snippets:
            serializer = CourseSerializer(c)
            data = serializer.data
            serializer2 = StudentSerializer(Student.objects.filter(course_id=c.id), many=True)
            data['student_count'] = len(serializer2.data)
            data_list.append(data)
        data = data_list[page_num*10-10:page_num*10]
        count = {
            "count": snippets.count(),
            "response": data,
            "all_data": data_list,
        }
        return Response(count)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCreateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = []

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
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


class CourseUpdateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
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
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        snippet = Course.objects.get(id=id)
        students = Student.objects.filter(course_id=id)
        for student in students:
            student.active = False
            student.save()
        snippet.active = False
        snippet.save()
        print(snippet.active)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchiveCourseListAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = []

    def get(self, request):
        snippets = Course.objects.filter(active=False)
        data_list = []
        page_num = int(self.request.query_params.get('page'))
        for c in snippets:
            serializer = CourseSerializer(c)
            data = serializer.data
            serializer2 = StudentSerializer(Student.objects.filter(course_id=c.id, active=False), many=True)
            data['student_count'] = len(serializer2.data)
            data_list.append(data)
        data = data_list[page_num*10-10:page_num*10]
        return Response(data)


class CourseDeleteAPIView(APIView):
    permission_classes = [IsSubAdminPermission]

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        students = Student.objects.filter(course_id=id)
        for student in students:
            student.delete()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseTypeListAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = []
    parser_classes = [JSONParser]

    def get(self, request):
        snippets = CourseType.objects.all()
        serializer = CourseTypeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseTypeDetailAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return CourseType.objects.get(id=id)
        except CourseType.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CourseTypeSerializer(snippet)
        data = serializer.data
        return Response(data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CourseTypeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
