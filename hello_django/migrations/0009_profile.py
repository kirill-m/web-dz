# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0008_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(default=b'Login', max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('nickname', models.CharField(default=b'nickname', max_length=100)),
                ('password', models.CharField(default=b'password', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
