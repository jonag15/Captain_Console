# Generated by Django 3.0.6 on 2020-05-10 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200509_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='maeyda',
        ),
    ]