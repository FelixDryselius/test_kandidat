# Generated by Django 2.0.3 on 2018-03-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_db_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
