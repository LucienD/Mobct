# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_google_maps.fields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cartography', '0008_category_placeholder_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Cat\xe9gorie', 'verbose_name_plural': 'Cat\xe9gories'},
        ),
        migrations.AlterModelOptions(
            name='pointofinterest',
            options={'verbose_name': "Point d'int\xe9r\xeat", 'verbose_name_plural': "Points d'int\xe9r\xeat"},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=b'cartography_category', verbose_name='Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Titre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='placeholder_image',
            field=models.ImageField(upload_to=b'cartography_category', verbose_name='Image de remplacement'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='address',
            field=django_google_maps.fields.AddressField(max_length=100, verbose_name='Adresse'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='category',
            field=models.ForeignKey(verbose_name='Cat\xe9gorie', to='cartography.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(max_length=100, verbose_name='G\xe9olocalisation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='image',
            field=models.ImageField(upload_to=b'cartography_pointOfInterest', verbose_name='Image', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='opening_hours',
            field=models.CharField(max_length=254, verbose_name="Heures d'ouverture", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='T\xe9l\xe9phone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='website',
            field=models.URLField(verbose_name='Site internet', blank=True),
            preserve_default=True,
        ),
    ]
