# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160518_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
