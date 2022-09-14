from django.db import models
from django.contrib.auth.models import User


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=255, null=True)


    def __str__(self):
        return f'{self.name} {self.second_name}'


class SubAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    second_name = models.CharField(max_length=100, null=False, blank=False)
    father_name = models.CharField(max_length=255, null=False, blank=False)
    personal_phone = models.CharField(max_length=255, null=False, blank=False)
    work_phone = models.CharField(max_length=255, null=False, blank=False)
    branch = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.second_name}'
