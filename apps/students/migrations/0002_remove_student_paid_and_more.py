# Generated by Django 4.1 on 2022-09-27 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='quantity_of_classes',
        ),
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
