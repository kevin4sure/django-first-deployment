# Generated by Django 2.1 on 2018-08-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='track_number',
            field=models.IntegerField(default=0),
        ),
    ]
