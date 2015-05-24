# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello_django', '0038_auto_20150519_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='ALike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voted', models.NullBooleanField(default=None)),
                ('answer', models.ForeignKey(to='hello_django.Answer')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='qlike',
            name='voted',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
    ]
