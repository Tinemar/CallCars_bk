# Generated by Django 3.0.1 on 2019-12-26 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='driver',
            field=models.CharField(default='', max_length=128, verbose_name='司机'),
        ),
        migrations.AddField(
            model_name='orders',
            name='driver_number',
            field=models.CharField(default='', max_length=128, verbose_name='司机车牌号'),
        ),
        migrations.AddField(
            model_name='orders',
            name='driver_phone',
            field=models.CharField(default='', max_length=128, verbose_name='司机手机号'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_phone',
            field=models.CharField(default='', max_length=128, verbose_name='用户手机号'),
        ),
    ]
