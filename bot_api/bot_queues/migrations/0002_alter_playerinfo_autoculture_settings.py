# Generated by Django 4.0.8 on 2023-02-08 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot_queues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerinfo',
            name='autoculture_settings',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='autoculture_settings', to='bot_queues.autoculturesettings'),
        ),
    ]
