import datetime

from django.db import models
from apps.mentor.models import Mentor


class Course(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    start_date = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.name