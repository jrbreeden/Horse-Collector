# Generated by Django 4.0.4 on 2022-07-27 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_horse_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='horse',
        ),
    ]
