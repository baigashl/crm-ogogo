from datetime import timedelta, datetime
import jwt
from django.contrib.auth.password_validation import validate_password
from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import SubAdmin
from django.contrib.auth.models import User as UserModel


JWT_SECRET = 'my_secret'  #   секретное слово для подписи
JWT_ACCESS_TTL = 60 * 5   # время жизни access токена в секундах (5 мин)
JWT_REFRESH_TTL = 3600 * 24 * 7 # время жизни refresh токена в секундах (неделя)


class LoginSerializer(serializers.Serializer):
    # ==== INPUT ====
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    # ==== OUTPUT ====
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        # standard validation
        validated_data = super().validate(attrs)

        # validate email and password
        username = validated_data['username']
        password = validated_data['password']
        error_msg = ('username or password are incorrect')
        try:
            user = UserModel.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError(error_msg)
            validated_data['user'] = user
        except UserModel.DoesNotExist:
            raise serializers.ValidationError(error_msg)

        return validated_data

    def create(self, validated_data):
        roles = [i.name for i in validated_data['user'].groups.all()]


        access_payload = {
            'iss': 'backend-api',
            'user_id': validated_data['user'].id,
            'exp': datetime.utcnow() + timedelta(seconds=JWT_ACCESS_TTL),
            'type': 'access',
            'role': roles[0]
        }
        access = jwt.encode(payload=access_payload, key=JWT_SECRET)

        refresh_payload = {
            'iss': 'backend-api',
            'user_id': validated_data['user'].id,
            'exp': datetime.utcnow() + timedelta(seconds=JWT_REFRESH_TTL),
            'type': 'refresh'
        }
        refresh = jwt.encode(payload=refresh_payload, key=JWT_SECRET)

        return {
            'access': access,
            'refresh': refresh
        }


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(
#         write_only=True,
#         required=True,
#         validators=[validate_password]
#     )
#     password2 = serializers.CharField(
#         write_only=True,
#         required=True
#     )
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password2', 'email']
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError(
#                 {"password": "Password fields didn`t match."}
#             )
#         return attrs
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


class SubAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = SubAdmin
        fields = [
            'id', 'username', 'name', 'second_name',
            'father_name', 'personal_phone', 'work_phone', 'branch',
            'password', 'password2'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn`t match."}
            )
        return attrs


class ListSubAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubAdmin
        fields = ['id', 'username', 'name', 'second_name', 'branch']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)
