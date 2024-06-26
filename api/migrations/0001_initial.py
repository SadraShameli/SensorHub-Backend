# Generated by Django 5.0.6 on 2024-06-12 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('location_name', models.CharField(max_length=100, unique=True)),
                ('location_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('unit', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('device_id', models.IntegerField(unique=True)),
                ('register_interval', models.IntegerField()),
                ('loudness_threshold', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
                ('sensors', models.ManyToManyField(to='api.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='recordings/')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.device')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('value', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.device')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sensor')),
            ],
        ),
    ]
