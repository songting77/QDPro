# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-20 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_auto_20180920_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='volumesetmodel',
            name='free_level',
            field=models.IntegerField(choices=[(0, '免费'), (1, 'VIP'), (2, '收费')], default=0, verbose_name='免费等级'),
        ),
    ]
