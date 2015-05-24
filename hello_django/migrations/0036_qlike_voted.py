# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0035_remove_qlike_voted'),
    ]

    operations = [
        migrations.AddField(
            model_name='qlike',
            name='voted',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
    ]
