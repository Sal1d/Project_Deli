# Generated by Django 4.1.1 on 2022-10-07 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_customuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
    ]
