# Generated by Django 3.0.6 on 2020-05-14 10:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200508_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('739eaa83-ffb4-4bbf-8042-b7a85f5fb059'), verbose_name='用户jwt加密秘钥'),
        ),
    ]