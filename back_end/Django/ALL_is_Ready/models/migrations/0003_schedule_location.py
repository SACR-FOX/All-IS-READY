# Generated by Django 3.2.7 on 2022-04-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20220406_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='Location',
            field=models.CharField(default='', max_length=20, verbose_name='上课地点'),
        ),
    ]
