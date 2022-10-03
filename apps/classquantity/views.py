from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework import permissions
from .models import ClassQuantity
from .serializers import ClassQuantitySerializer, StudentClassQuantitySerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import ClassQuantity, StudentClassQuantity
from apps.mentor.models import Mentor
from apps.administrator.permissions import IsSubAdminPermission


class ClassQuantityListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = ClassQuantity.objects.all()
        serializer = ClassQuantitySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassQuantitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassQuantityCreateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = []

    def post(self, request):
        serializer = ClassQuantitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassQuantityDetailAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return ClassQuantity.objects.filter(mentor_id=id)
        except ClassQuantity.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ClassQuantitySerializer(snippet, many=True)
        data = serializer.data
        return Response(data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ClassQuantitySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassQuantityUpdateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return ClassQuantity.objects.get(mentor_id=id)
        except ClassQuantity.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ClassQuantitySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassQuantityDeleteAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return ClassQuantity.objects.get(mentor_id=id)
        except ClassQuantity.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#############################################################################33


class StudentClassQuantityListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = StudentClassQuantity.objects.all()
        serializer = StudentClassQuantitySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentClassQuantitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentClassQuantityCreateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = []

    def post(self, request):
        serializer = StudentClassQuantitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentClassQuantityDetailAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]


    def get_objects(self, stud_id):
        try:
            return StudentClassQuantity.objects.filter(student_id=stud_id)
        except StudentClassQuantity.DoesNotExist:
            raise Http404

    def get_object(self, stud_id, course_id):
        try:
            return StudentClassQuantity.objects.get(student_id=stud_id, course_id=course_id)
        except StudentClassQuantity.DoesNotExist:
            raise Http404

    def get(self, request, stud_id,  format=None):
        snippet = self.get_objects(stud_id)
        serializer = StudentClassQuantitySerializer(snippet, many=True)
        data = serializer.data
        return Response(data)

    def put(self, request, stud_id, course_id, format=None):
        snippet = self.get_object(stud_id, course_id)
        serializer = StudentClassQuantitySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentClassQuantityUpdateAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, stud_id, course_id):
        try:
            return StudentClassQuantity.objects.get(student_id=stud_id, course_id=course_id)
        except StudentClassQuantity.DoesNotExist:
            raise Http404

    def put(self, request, stud_id, course_id, format=None):
        snippet = self.get_object(stud_id, course_id)
        serializer = StudentClassQuantitySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentClassQuantityDeleteAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return StudentClassQuantity.objects.get(mentor_id=id)
        except StudentClassQuantity.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
