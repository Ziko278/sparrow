# Generated by Django 3.2.9 on 2021-12-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparrow_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolsmodel',
            name='status',
            field=models.CharField(blank=True, default='new', max_length=15),
        ),
    ]
