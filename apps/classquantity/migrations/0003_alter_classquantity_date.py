# Generated by Django 4.1 on 2022-08-30 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classquantity', '0002_alter_classquantity_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classquantity',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 30, 13, 45, 0, 662244), null=True),
        ),
    ]
