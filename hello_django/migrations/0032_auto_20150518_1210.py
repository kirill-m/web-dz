# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0031_auto_20150518_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='like',
            field=models.ForeignKey(to='hello_django.Like'),
            preserve_default=True,
        ),
    ]
