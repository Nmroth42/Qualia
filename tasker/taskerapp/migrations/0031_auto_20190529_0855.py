# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-29 08:55
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskerapp', '0030_remove_profile_philosopher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gig',
            name='tasks',
        ),
        migrations.AddField(
            model_name='gig',
            name='questions',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
