# Generated by Django 3.2.9 on 2021-12-19 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_classesmodel_form_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='classesmodel',
            name='assistant_form_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assistant_form_teacher', to='registration.staffmodel'),
        ),
    ]
