# Generated by Django 2.0.4 on 2019-07-03 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0009_dumpwhitelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dumpwhitelist',
            name='comment',
        ),
    ]