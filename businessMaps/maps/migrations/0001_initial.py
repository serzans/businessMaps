# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_text', models.CharField(max_length=200)),
            ],
        ),
    ]
