# Generated by Django 3.2.9 on 2021-12-19 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20211218_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='parentsmodel',
            name='status',
            field=models.CharField(blank=True, default='active', max_length=15),
        ),
        migrations.AddField(
            model_name='staffmodel',
            name='registration_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staffmodel',
            name='status',
            field=models.CharField(blank=True, default='active', max_length=15),
        ),
        migrations.AlterField(
            model_name='parentsmodel',
            name='religion',
            field=models.CharField(choices=[('', 'SELECT YOUR RELIGION'), ('c', 'CHRISTIANITY'), ('i', 'ISLAM'), ('o', 'OTHERS')], max_length=3),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='religion',
            field=models.CharField(choices=[('c', 'SELECT YOUR RELIGION'), ('c', 'CHRISTIANITY'), ('i', 'ISLAM'), ('o', 'OTHERS')], max_length=3),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='section',
            field=models.CharField(choices=[('', ''), ('a', 'Academic'), ('n', 'Non Academic')], max_length=20),
        ),
        migrations.CreateModel(
            name='StudentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=50)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/staff_images')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('religion', models.CharField(choices=[('c', 'SELECT YOUR RELIGION'), ('c', 'CHRISTIANITY'), ('i', 'ISLAM'), ('o', 'OTHERS')], max_length=3)),
                ('nationality', models.CharField(default='Nigerian', max_length=100)),
                ('state_of_origin', models.CharField(blank=True, choices=[('', ''), ('ab', 'ABIA'), ('an', 'ANAMBRA'), ('be', 'BENUE'), ('cr', 'CROSS RIVER')], max_length=50, null=True)),
                ('lga', models.CharField(blank=True, choices=[('', ''), ('ab', 'ABIA'), ('an', 'ANAMBRA'), ('be', 'BENUE'), ('cr', 'CROSS RIVER')], max_length=50, null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, default='active', max_length=15)),
                ('previous_classes', models.JSONField(blank=True, null=True)),
                ('parents', models.ManyToManyField(to='registration.ParentsModel')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.classesmodel')),
            ],
        ),
    ]