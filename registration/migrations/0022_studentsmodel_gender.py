# Generated by Django 3.2.9 on 2022-01-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_parentsmodel_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsmodel',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], default='male', max_length=10),
            preserve_default=False,
        ),
    ]
