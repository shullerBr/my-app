# Generated by Django 2.0.9 on 2018-11-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_auto_20181126_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='beat_points',
            field=models.IntegerField(default=0),
        ),
    ]