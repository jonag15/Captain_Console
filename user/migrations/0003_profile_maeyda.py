# Generated by Django 3.0.6 on 2020-05-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200509_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='maeyda',
            field=models.CharField(default='qqq', max_length=255),
            preserve_default=False,
        ),
    ]