# Generated by Django 4.1.3 on 2022-11-20 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_carmarks_options_alter_firms_options_cars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmarks',
            old_name='name',
            new_name='name_car_marks',
        ),
        migrations.RenameField(
            model_name='firms',
            old_name='name',
            new_name='name_firms',
        ),
    ]
