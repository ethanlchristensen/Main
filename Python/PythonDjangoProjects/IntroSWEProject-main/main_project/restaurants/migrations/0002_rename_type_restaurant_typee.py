# Generated by Django 3.2 on 2021-04-27 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='type',
            new_name='typee',
        ),
    ]