# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ufaculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='stuClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'stuClass',
                'managed': False,
            },
        ),
    ]
