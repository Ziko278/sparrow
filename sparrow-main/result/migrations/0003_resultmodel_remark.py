# Generated by Django 4.0.1 on 2022-01-31 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_resultmodel_assignment_resultmodel_exam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultmodel',
            name='remark',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]