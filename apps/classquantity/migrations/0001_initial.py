# Generated by Django 4.1 on 2022-08-30 13:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 30, 13, 33, 11, 896674), null=True)),
                ('quantity_of_classes', models.IntegerField(blank=True, null=True)),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mentor.mentor')),
            ],
        ),
    ]
