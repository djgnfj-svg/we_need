# Generated by Django 4.0.3 on 2022-03-13 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_myuser_full_name_myuser_nick_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='nick_name',
            new_name='nickname',
        ),
    ]