# Generated by Django 4.1 on 2022-08-06 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 6, 12, 0, 53, 608430), null=True),
        ),
    ]