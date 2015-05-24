# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0037_auto_20150519_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qlike',
            name='question',
            field=models.ForeignKey(to='hello_django.Question'),
            preserve_default=True,
        ),
    ]
