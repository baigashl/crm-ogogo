from django.db import models
from apps.mentor.models import Mentor
from apps.students.models import Student
from apps.course.models import Course
import datetime


class ClassQuantity(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    quantity_of_classes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.date}'


class StudentClassQuantity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    quantity_of_classes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.student}, {self.date}'
