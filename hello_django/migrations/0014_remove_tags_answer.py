# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0013_auto_20150429_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='answer',
        ),
    ]
