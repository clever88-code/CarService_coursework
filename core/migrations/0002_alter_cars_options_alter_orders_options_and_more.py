# Generated by Django 4.1.3 on 2022-11-28 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='records',
            options={'managed': False},
        ),
    ]
