# Generated by Django 3.2.9 on 2021-12-08 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meetings',
            new_name='Meeting',
        ),
    ]