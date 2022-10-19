# Generated by Django 2.2.14 on 2022-10-19 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('code', models.CharField(editable=False, max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=10)),
                ('lower', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('upper', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]
