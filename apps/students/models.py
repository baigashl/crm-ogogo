from django.db import models
from apps.course.models import Course


class Student(models.Model):
    course = models.ManyToManyField(Course, blank=True)
    email = models.EmailField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    second_name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=50, null=True)
    first_month_paid = models.IntegerField(default=0)
    second_month_paid = models.IntegerField(default=0)
    third_month_paid = models.IntegerField(default=0)
    fourth_month_paid = models.IntegerField(default=0)
    description = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qrcode', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'
