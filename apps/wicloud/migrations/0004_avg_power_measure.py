# Generated by Django 2.0 on 2019-03-07 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wicloud', '0003_auto_20190305_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avg_Power_Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_modified_date', models.DateTimeField(auto_now=True, verbose_name='Last modified date')),
                ('status', models.IntegerField(choices=[(0, 'disabled'), (1, 'enabled')], default=1, null=True, verbose_name='status')),
                ('ordering', models.IntegerField(default=0, verbose_name='ordering')),
                ('mac', models.CharField(max_length=255)),
                ('hms', models.CharField(blank=True, max_length=255, null=True)),
                ('nodeDate', models.CharField(blank=True, max_length=255, null=True)),
                ('vac', models.FloatField(blank=True, null=True)),
                ('iac', models.FloatField(blank=True, null=True)),
                ('activePower', models.FloatField(blank=True, null=True)),
                ('reactivePower', models.FloatField(blank=True, null=True)),
                ('intervalActiveEnergy', models.FloatField(blank=True, null=True)),
                ('intervalReactiveEnergy', models.FloatField(blank=True, null=True)),
                ('intervalBurningTime', models.FloatField(blank=True, null=True)),
                ('intervalNodeLife', models.FloatField(blank=True, null=True)),
                ('pw0', models.FloatField(blank=True, null=True)),
                ('pw1', models.FloatField(blank=True, null=True)),
                ('pw2', models.FloatField(blank=True, null=True)),
                ('pw3', models.FloatField(blank=True, null=True)),
                ('activeEnergyCounter', models.FloatField(blank=True, null=True)),
                ('reactiveEnergyCounter', models.FloatField(blank=True, null=True)),
                ('burningTime', models.FloatField(blank=True, null=True)),
                ('nodeLife', models.FloatField(blank=True, null=True)),
                ('ad0', models.FloatField(blank=True, null=True)),
                ('ad1', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('lqi', models.FloatField(blank=True, null=True)),
                ('pks', models.FloatField(blank=True, null=True)),
                ('pkr', models.FloatField(blank=True, null=True)),
                ('pkl', models.FloatField(blank=True, null=True)),
                ('_node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='avgPowerMeasures', to='wicloud.Node')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wicloud_avg_power_measure_creator', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('installation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='avgPowerMeasures', to='wicloud.Installation')),
                ('last_modifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wicloud_avg_power_measure_last_modifier', to=settings.AUTH_USER_MODEL, verbose_name='last modifier')),
                ('lightFixture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='avgPowerMeasures', to='wicloud.Light_fixture')),
                ('lightManagementModule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='avgPowerMeasures', to='wicloud.Light_management_module')),
            ],
            options={
                'verbose_name': 'avg_power_measure',
                'verbose_name_plural': 'avg_power_measures',
                'ordering': ('ordering',),
                'permissions': (('list_avg_power_measure', 'Can list AvgPower measure'), ('detail_avg_power_measure', 'Can detail AvgPower measure'), ('disable_avg_power_measure', 'Can disable AvgPower measure')),
            },
        ),
    ]
