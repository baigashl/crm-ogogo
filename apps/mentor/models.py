from django.db import models


class Mentor(models.Model):
    name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=30, null=False, blank=True)
    quantiy_of_classes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name
