# Generated by Django 3.2.7 on 2022-04-13 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0014_alter_communitytopic_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicpost',
            name='Time',
            field=models.IntegerField(verbose_name='创建时间'),
        ),
    ]