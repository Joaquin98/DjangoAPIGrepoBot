# Generated by Django 4.0.8 on 2023-02-07 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssistantSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town_names', models.BooleanField()),
                ('player_name', models.BooleanField()),
                ('alliance_name', models.BooleanField()),
                ('auto_relogin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AutoBuildSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autostart', models.BooleanField()),
                ('enable_building', models.BooleanField()),
                ('enable_units', models.BooleanField()),
                ('enable_ships', models.BooleanField()),
                ('timeinterval', models.IntegerField()),
                ('instant_buy', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AutoCultureSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autostart', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AutoFarmSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autostart', models.BooleanField()),
                ('method', models.IntegerField()),
                ('timebetween', models.IntegerField()),
                ('skipwhenfull', models.BooleanField()),
                ('lowresfirst', models.BooleanField()),
                ('stoplootbelow', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField()),
                ('party', models.BooleanField()),
                ('triumph', models.BooleanField()),
                ('theater', models.BooleanField()),
                ('auto_culture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.autoculturesettings')),
            ],
        ),
        migrations.CreateModel(
            name='UnitsOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.city')),
            ],
        ),
        migrations.CreateModel(
            name='ShipOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.city')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('premium_time', models.IntegerField()),
                ('trial_time', models.IntegerField()),
                ('facebook_like', models.IntegerField()),
                ('assistant_settings', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.assistantsettings')),
                ('autobuild_settings', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.autobuildsettings')),
                ('autoculture_settings', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.autoculturesettings')),
                ('autofarm_settings', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.autofarmsettings')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.playerinfo'),
        ),
        migrations.CreateModel(
            name='BuildingOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('player_id', models.IntegerField()),
                ('player_world', models.CharField(max_length=20)),
                ('town_id', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('item_name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('added', models.DateTimeField()),
                ('City', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bot_queues.city')),
            ],
        ),
    ]
