# Generated by Django 4.1 on 2022-08-30 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('paid', models.IntegerField(default=0)),
                ('first_month_paid', models.IntegerField(default=0)),
                ('second_month_paid', models.IntegerField(default=0)),
                ('third_month_paid', models.IntegerField(default=0)),
                ('fourth_month_paid', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
                ('quantity_of_classes', models.IntegerField(blank=True, default=0, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course')),
            ],
        ),
    ]
