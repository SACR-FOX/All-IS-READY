# Generated by Django 3.2.7 on 2022-04-21 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0017_auto_20220421_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemodel',
            old_name='Filename',
            new_name='FileName',
        ),
    ]
