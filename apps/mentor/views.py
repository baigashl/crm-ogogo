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


class MentorListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = Mentor.objects.all()
        serializer = MentorSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def post(self, request, format=None):
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Mentor.objects.get(id=id)
        except Mentor.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = MentorSerializer(snippet)
        data = serializer.data
        return Response(data)

    def put(self, request, id, format=None):
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
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return Mentor.objects.get(id=id)
        except Mentor.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MentorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorDeleteAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


