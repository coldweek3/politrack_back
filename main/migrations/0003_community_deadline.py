# Generated by Django 4.2.7 on 2023-11-06 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_community_name_alter_community_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 15, 59, 36, 838400, tzinfo=datetime.timezone.utc)),
        ),
    ]
