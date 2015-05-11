# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0014_remove_tags_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='login',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
