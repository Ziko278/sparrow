# Generated by Django 3.2.9 on 2021-12-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('line_one', models.BigIntegerField()),
                ('line_two', models.BigIntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('pri', 'PRIMARY SCHOOL'), ('sec', 'SECONDARY SCHOOL'), ('mix', 'COMBINED SCHOOL')], max_length=5)),
                ('applicant_name', models.CharField(max_length=100)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('applicant_phone', models.BigIntegerField()),
                ('applicant_position', models.CharField(choices=[('o', 'SCHOOL OWNER'), ('d', 'SCHOOL DIRECTOR'), ('s', 'SCHOOL STAFF'), ('ot', 'OTHER')], max_length=5)),
                ('status', models.CharField(default='new', max_length=15)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('activation_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
