# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0024_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'test_tag', max_length=20)),
                ('question', models.ManyToManyField(to='hello_django.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
