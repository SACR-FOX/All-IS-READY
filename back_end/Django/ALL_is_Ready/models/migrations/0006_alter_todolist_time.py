# Generated by Django 3.2.7 on 2022-04-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20220407_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='Time',
            field=models.IntegerField(default=0, verbose_name='提醒时间'),
        ),
    ]