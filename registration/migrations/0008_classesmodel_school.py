# Generated by Django 3.2.9 on 2021-12-28 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sparrow_admin', '0003_auto_20211218_1143'),
        ('registration', '0007_classesmodel_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='classesmodel',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sparrow_admin.schoolsmodel'),
            preserve_default=False,
        ),
    ]
