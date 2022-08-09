from django.db import models


class Administrator(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.name} {self.second_name}'


