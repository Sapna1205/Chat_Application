# Generated by Django 4.0.1 on 2022-01-18 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='msg',
            new_name='value',
        ),
    ]
