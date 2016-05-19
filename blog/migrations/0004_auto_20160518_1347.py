# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160518_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
