# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0019_auto_20151023_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carpool',
            options={'verbose_name': 'Covoiturage', 'verbose_name_plural': 'Covoiturages'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'Inscription', 'verbose_name_plural': 'Inscriptions'},
        ),
        migrations.AlterField(
            model_name='carpool',
            name='arrival_latitude',
            field=models.FloatField(verbose_name='Arriv\xe9e - latitude'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='arrival_longitude',
            field=models.FloatField(verbose_name='Arriv\xe9e - longitude'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='cancelled',
            field=models.BooleanField(default=False, verbose_name='Annul\xe9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='comment',
            field=models.TextField(verbose_name='Commentaire', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='creation_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de cr\xe9ation', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='departure_latitude',
            field=models.FloatField(verbose_name='D\xe9part - latitude'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='departure_longitude',
            field=models.FloatField(verbose_name='D\xe9part - longitude'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='free',
            field=models.BooleanField(default=True, verbose_name='Covoiturage gratuit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='frequency',
            field=models.CharField(default=b'OCC', max_length=3, verbose_name='Fr\xe9quence', choices=[(b'OCC', 'Ponctuel'), (b'REG', 'R\xe9gulier')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='occ_arrival_datetime',
            field=models.DateTimeField(null=True, verbose_name="Date d'arriv\xe9e", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='occ_departure_datetime',
            field=models.DateTimeField(null=True, verbose_name='Date de d\xe9part', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='reg_arrival_time',
            field=models.TimeField(null=True, verbose_name="Heure d'arriv\xe9e", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='reg_departure_time',
            field=models.TimeField(null=True, verbose_name='Heure de d\xe9part', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='seats_number',
            field=models.PositiveSmallIntegerField(max_length=10, verbose_name='Places disponibles', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (None, 'Places disponibles')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='update_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de mise \xe0 jour', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='accepted',
            field=models.NullBooleanField(default=None, verbose_name='Accept\xe9e'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='cancelled',
            field=models.BooleanField(default=False, verbose_name='Annul\xe9e'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='carpool',
            field=models.ForeignKey(verbose_name='Covoiturage', to='carpooling.Carpool'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='creation_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de cr\xe9ation', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscriber',
            field=models.ForeignKey(verbose_name='Inscrit', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='update_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de mise \xe0 jour', blank=True),
            preserve_default=True,
        ),
    ]
