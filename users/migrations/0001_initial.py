# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-13 04:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('url', models.URLField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('source', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('picture', models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fav_list', models.ManyToManyField(to='users.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
