# Generated by Django 4.1 on 2022-09-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='qr_code',
            field=models.ImageField(default=1, upload_to='qrcode'),
            preserve_default=False,
        ),
    ]
