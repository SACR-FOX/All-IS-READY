# Generated by Django 3.2.7 on 2022-04-21 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0018_rename_filename_filemodel_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemodel',
            old_name='FoldName',
            new_name='FolderName',
        ),
    ]
