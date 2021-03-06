# Generated by Django 3.0.4 on 2020-04-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0023_auto_20200401_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callevent',
            name='participant_id',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='callevent',
            name='participant_status',
            field=models.CharField(blank=True, choices=[('connected', 'connected'), ('disconnected', 'disconnected')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='callevent',
            name='track_kind',
            field=models.CharField(blank=True, choices=[('data', 'data'), ('audio', 'audio'), ('video', 'video')], max_length=20, null=True),
        ),
    ]
