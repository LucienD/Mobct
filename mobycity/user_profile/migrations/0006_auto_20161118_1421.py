# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20151112_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='T\xe9l\xe9phone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'user_profile_userProfile', null=True, verbose_name=b'Photo', blank=True),
            preserve_default=True,
        ),
    ]
