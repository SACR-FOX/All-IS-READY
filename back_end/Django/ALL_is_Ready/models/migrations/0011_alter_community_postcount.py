# Generated by Django 3.2.7 on 2022-04-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0010_alter_community_renewal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='PostCount',
            field=models.IntegerField(default=0, verbose_name='帖子数'),
        ),
    ]