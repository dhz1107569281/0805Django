# Generated by Django 2.1.8 on 2019-10-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identity',
            field=models.IntegerField(default=0),
        ),
    ]
