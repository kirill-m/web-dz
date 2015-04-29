# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0011_auto_20150428_1644'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.AddField(
            model_name='tags',
            name='question',
            field=models.ManyToManyField(to='hello_django.Question'),
            preserve_default=True,
        ),
    ]
