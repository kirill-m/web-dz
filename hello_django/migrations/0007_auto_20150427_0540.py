# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0006_auto_20150427_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.CharField(default=b'test_tag', max_length=20),
            preserve_default=True,
        ),
    ]
