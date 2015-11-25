# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20151123_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='value',
            field=models.DecimalField(help_text=b'How much this opportunity is worth to the organization', max_digits=10, decimal_places=2),
        ),
    ]
