# Generated by Django 3.2.9 on 2021-12-29 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_staffmodel_relationship_with_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffmodel',
            name='relationship_with_student',
        ),
        migrations.AddField(
            model_name='parentsmodel',
            name='relationship_with_student',
            field=models.CharField(choices=[('father', 'FATHER'), ('mother', 'MOTHER')], default='father', max_length=20),
            preserve_default=False,
        ),
    ]
