# Generated by Django 3.2.9 on 2022-01-10 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0023_auto_20220109_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsmodel',
            name='gender',
        ),
    ]
