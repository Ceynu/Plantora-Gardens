# Generated by Django 5.0.6 on 2024-05-28 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('s_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.student')),
                ('t_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.teacher')),
            ],
        ),
    ]