# Generated by Django 3.2.7 on 2022-04-28 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0026_communitystars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitytopic',
            old_name='Creator',
            new_name='UID',
        ),
    ]
