# Generated by Django 4.0.5 on 2022-08-03 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_action_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='coordinationlist',
            new_name='coordinationaction',
        ),
        migrations.RemoveField(
            model_name='action',
            name='contact',
        ),
    ]