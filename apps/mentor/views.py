from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Mentor
from .serializers import MentorSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from apps.course.models import Course
from apps.course.serializers import CourseSerializer
from apps.administrator.permissions import IsSubAdminPermission
from apps.classquantity.models import ClassQuantity


class MentorListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, id):
        try:
            return Mentor.objects.get(id=id)
        except Mentor.DoesNotExist:
            raise Http404

    def get(self, request):
        snippets = Mentor.objects.all()
        data_list = []
        for c in snippets:
            serializer = MentorSerializer(c)
            data = serializer.data
            class_quan = ClassQuantity.objects.filter(mentor_id=c.id)
            quan = 0
            for i in class_quan:
                quan += i.quantity_of_classes
            data['quantiy_of_classes'] = quan
            data_list.append(data)
        return Response(data_list)



    def post(self, request, format=None):
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorCreateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = []

    def post(self, request, format=None):
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorDetailAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Mentor.objects.get(id=id)
        except Mentor.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        course = Course.objects.filter(mentor_id=id)
        serializer = MentorSerializer(snippet)
        serializer2 = CourseSerializer(course, many=True)
        data = serializer.data
        data['course'] = serializer2.data
        return Response(data)

    def put(self, request, id):
        snippet = self.get_object(id)
        serializer = MentorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MentorUpdateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Mentor.objects.get(id=id)
        except Mentor.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = MentorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorDeleteAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Mentor.objects.get(id=id)
        except Mentor.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


