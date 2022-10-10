from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from .serializers import ListSubAdminSerializer, SubAdminSerializer
from .permissions import AnonPermissionOnly
from rest_framework import permissions
from .models import SubAdmin
from .permissions import IsAdminPermission


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer

# class MyObtainPairView(APIView):
#     permission_classes = (AnonPermissionOnly,)
#
#     def post(self, request, format=None):
#         serializer = MyTokenObtainPairSerializer(data=request.data)
#         if serializer.is_valid():
#             response_data = serializer.save()
#             return Response(response_data)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateSubAdminView(APIView):
    permission_classes = [IsAdminPermission]
    # authentication_classes = []

    def post(self, request):
        serializer = SubAdminSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                username=request.data['username']
            )
            user.set_password(request.data['password'])
            user.save()
            subadmin = SubAdmin.objects.create(
                user=user,
                username=request.data['username'],
                name=request.data['name'],
                second_name=request.data['second_name'],
                father_name=request.data['father_name'],
                work_phone=request.data['work_phone'],
                personal_phone=request.data['personal_phone'],
                branch=request.data['branch']
            )
            subadmin.save()
            my_admin_group = Group.objects.get_or_create(name='SUBADMIN')
            my_admin_group[0].user_set.add(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubAdminListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = SubAdmin.objects.all()
        serializer = ListSubAdminSerializer(snippets, many=True)
        return Response(serializer.data)


class SubAdminDeleteAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]

    def get_object(self, id):
        try:
            return SubAdmin.objects.get(id=id)
        except SubAdmin.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
