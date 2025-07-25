# Generated by Django 5.1 on 2024-10-24 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='locations.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('producer', 'Producer'), ('consumer', 'Consumer')], default='producer', max_length=10),
        ),
    ]
