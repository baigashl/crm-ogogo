# Generated by Django 4.1 on 2022-08-08 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_course_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 8, 11, 57, 2, 410912), null=True),
        ),
    ]