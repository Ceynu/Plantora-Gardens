# Generated by Django 5.1 on 2024-08-15 19:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_plantshop_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='ordered_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
