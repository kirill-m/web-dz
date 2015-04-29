# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0009_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='tags',
            new_name='tag',
        ),
    ]
