# Generated by Django 4.1 on 2022-08-30 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classquantity', '0004_alter_classquantity_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classquantity',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 30, 13, 51, 33, 966940), null=True),
        ),
    ]
