from django.db import models
from apps.mentor.models import Mentor
import datetime


class ClassQuantity(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)
    quantity_of_classes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.date}'

