# Generated by Django 5.0.6 on 2024-06-03 15:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cjajb', '0005_category_alter_meeting_championship_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='date',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='time',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='category',
            name='short_name',
            field=models.CharField(default='a', max_length=16, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='organizer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='cjajb.team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='season',
            field=models.CharField(choices=[('O', 'Outdoor'), ('I', 'Indoor')], default='O', max_length=1),
            preserve_default=False,
        ),
    ]
