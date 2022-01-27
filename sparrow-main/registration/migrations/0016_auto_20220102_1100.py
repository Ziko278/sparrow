# Generated by Django 3.2.9 on 2022-01-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20220102_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsmodel',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentsmodel',
            name='nationality',
            field=models.CharField(blank=True, default='Nigerian', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentsmodel',
            name='registration_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentsmodel',
            name='religion',
            field=models.CharField(blank=True, choices=[('c', 'CHRISTIANITY'), ('i', 'ISLAM'), ('o', 'OTHERS')], max_length=3, null=True),
        ),
    ]
