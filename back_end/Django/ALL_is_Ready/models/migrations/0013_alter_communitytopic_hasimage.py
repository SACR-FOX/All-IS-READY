# Generated by Django 3.2.7 on 2022-04-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_alter_community_renewal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitytopic',
            name='HasImage',
            field=models.BooleanField(default=False, verbose_name='是否含有图片'),
        ),
    ]
