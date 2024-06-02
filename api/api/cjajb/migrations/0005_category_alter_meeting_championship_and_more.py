# Generated by Django 5.0.6 on 2024-06-02 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cjajb', '0004_venue_meeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age_limit', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='meeting',
            name='championship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='cjajb.championship'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='cjajb.venue'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='athletes', to='cjajb.category'),
            preserve_default=False,
        ),
    ]
