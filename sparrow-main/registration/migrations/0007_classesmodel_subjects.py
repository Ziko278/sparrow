# Generated by Django 3.2.9 on 2021-12-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
        ('registration', '0006_classesmodel_assistant_form_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='classesmodel',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='basic.SubjectsModel'),
        ),
    ]