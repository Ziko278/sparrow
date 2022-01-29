# Generated by Django 3.2.9 on 2022-01-09 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sparrow_admin', '0004_delete_schoolmodel'),
        ('registration', '0020_auto_20220109_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentsmodel',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sparrow_admin.schoolsmodel'),
            preserve_default=False,
        ),
    ]
