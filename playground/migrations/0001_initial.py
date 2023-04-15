# Generated by Django 4.2 on 2023-04-15 04:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('creation', models.DateField(default=datetime.datetime.today, verbose_name='Date')),
                ('completion', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('COMPLETE', 'Complete')], default='INACTIVE', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='TasksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('creation', models.DateField(default=datetime.datetime.today, verbose_name='Date')),
                ('completion', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('COMPLETE', 'Complete')], default='INACTIVE', max_length=8)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.projectsmodel')),
            ],
        ),
    ]
