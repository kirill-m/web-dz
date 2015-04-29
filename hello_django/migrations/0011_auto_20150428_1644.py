# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0010_auto_20150428_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='tag',
            new_name='tags',
        ),
    ]
