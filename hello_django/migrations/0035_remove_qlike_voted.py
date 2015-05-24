# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0034_auto_20150518_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qlike',
            name='voted',
        ),
    ]
