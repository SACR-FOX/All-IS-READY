# Generated by Django 3.2.7 on 2022-04-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='UID',
            field=models.IntegerField(default=-1, verbose_name='所属用户ID'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='Tag',
            field=models.IntegerField(default=0, verbose_name='标签颜色'),
        ),
    ]
