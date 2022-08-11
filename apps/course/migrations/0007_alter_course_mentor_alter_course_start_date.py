# Generated by Django 4.1 on 2022-08-08 11:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_mentor_phone_alter_mentor_quantiy_of_classes'),
        ('course', '0006_alter_course_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mentor.mentor'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 8, 11, 25, 21, 763992), null=True),
        ),
    ]