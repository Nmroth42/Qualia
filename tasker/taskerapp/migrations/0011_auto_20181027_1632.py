# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-27 16:32
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskerapp', '0010_auto_20181027_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]