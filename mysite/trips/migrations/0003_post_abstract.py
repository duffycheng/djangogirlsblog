# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20150825_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='abstract',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
