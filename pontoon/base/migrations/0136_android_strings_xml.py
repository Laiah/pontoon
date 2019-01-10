# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0135_project_project_configuration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='format',
            field=models.CharField(blank=True, choices=[('dtd', 'dtd'), ('ftl', 'ftl'), ('inc', 'inc'), ('ini', 'ini'), ('json', 'json'), ('lang', 'lang'), ('po', 'po'), ('properties', 'properties'), ('xlf', 'xliff'), ('xliff', 'xliff'), ('xml', 'xml')], max_length=20, verbose_name='Format'),
        ),
    ]