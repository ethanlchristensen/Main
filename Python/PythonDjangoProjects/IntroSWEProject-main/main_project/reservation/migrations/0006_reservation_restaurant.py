# Generated by Django 3.2 on 2021-04-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_alter_reservation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='restaurant',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
