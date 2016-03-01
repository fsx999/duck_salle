# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duck_utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=128, null=True, blank=True)),
                ('date', models.DateField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('salle', models.ForeignKey(to='duck_utils.Salle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
