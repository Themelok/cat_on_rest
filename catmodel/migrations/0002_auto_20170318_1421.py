# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import catmodel.models


class Migration(migrations.Migration):

    dependencies = [
        ('catmodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='image',
            field=models.ImageField(upload_to=catmodel.models.scramble, verbose_name=b'Uploaded image'),
        ),
    ]
