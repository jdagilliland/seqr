# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-13 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_individual_review_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='review_status',
            new_name='case_review_status',
        ),
        migrations.AddField(
            model_name='individual',
            name='in_case_review',
            field=models.BooleanField(default=False),
        ),
    ]
