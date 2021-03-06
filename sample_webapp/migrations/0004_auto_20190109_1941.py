# Generated by Django 2.0.7 on 2019-01-09 19:41

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_webapp', '0003_foo_geojson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foo',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'example': 1.1}),
        ),
        migrations.AlterField(
            model_name='foo',
            name='geojson',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
