# Generated by Django 4.2 on 2024-08-21 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_options_remove_users_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='users',
            name='country',
        ),
        migrations.RemoveField(
            model_name='users',
            name='token',
        ),
    ]