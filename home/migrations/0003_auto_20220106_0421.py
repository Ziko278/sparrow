# Generated by Django 3.2.9 on 2022-01-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newslettermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteinfomodel',
            name='site_social_youtube',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='websiteinfomodel',
            name='site_social_youtube_video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
