# Generated by Django 4.0.4 on 2023-03-12 22:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot_queues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingorder',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 22, 8, 7, 392563, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='premium_time',
            field=models.IntegerField(blank=True, default=1679263687.0, null=True),
        ),
        migrations.AlterField(
            model_name='premium',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 12, 22, 8, 7, 393969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shiporder',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 22, 8, 7, 393588, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='unitorder',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 22, 8, 7, 392966, tzinfo=utc)),
        ),
    ]
