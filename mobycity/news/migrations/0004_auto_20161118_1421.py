# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20151030_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Actualit\xe9', 'verbose_name_plural': 'Actualit\xe9s'},
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=djangocms_text_ckeditor.fields.HTMLField(verbose_name='Contenu'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='creation_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de cr\xe9ation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=b'news_news', verbose_name='Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='link1',
            field=models.URLField(verbose_name='Lien 1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='link2',
            field=models.URLField(verbose_name='Lien 2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='link3',
            field=models.URLField(verbose_name='Lien 3', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='publication_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de publication'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='subtitle',
            field=models.CharField(max_length=255, verbose_name='Sous-titre', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='theme',
            field=models.CharField(max_length=100, verbose_name='Th\xe8me'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='update_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de mise \xe0 jour'),
            preserve_default=True,
        ),
    ]
