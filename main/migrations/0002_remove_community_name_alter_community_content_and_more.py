# Generated by Django 4.2.7 on 2023-11-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='name',
        ),
        migrations.AlterField(
            model_name='community',
            name='content',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
