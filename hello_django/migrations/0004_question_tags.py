# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0003_question_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=20),
            preserve_default=True,
        ),
    ]
