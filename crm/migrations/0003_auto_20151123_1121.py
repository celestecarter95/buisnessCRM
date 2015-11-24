# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20151123_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opportunity',
            old_name='sourse',
            new_name='source',
        ),
    ]
