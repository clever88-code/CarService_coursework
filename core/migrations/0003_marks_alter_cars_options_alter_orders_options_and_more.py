# Generated by Django 4.1.3 on 2022-11-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cars_options_alter_orders_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_avto', models.TextField(verbose_name='Описание проблемы')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cars',
            options={'managed': False, 'verbose_name': 'автомобиль', 'verbose_name_plural': 'Список автомобилей'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': False, 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы Выполненые'},
        ),
        migrations.AlterModelOptions(
            name='records',
            options={'managed': False, 'verbose_name': 'запись', 'verbose_name_plural': 'Записи'},
        ),
    ]
