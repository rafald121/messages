# Generated by Django 3.1.3 on 2020-11-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0002_auto_20201113_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
