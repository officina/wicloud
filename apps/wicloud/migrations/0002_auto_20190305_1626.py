# Generated by Django 2.0 on 2019-03-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wicloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='energy_interval',
            name='adcValue0',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energy_interval',
            name='adcValue1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energy_interval',
            name='dimLevel',
            field=models.FloatField(blank=True, null=True),
        ),
    ]