# Generated by Django 5.0.6 on 2024-06-30 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='booking',
            table='booking',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='menu',
        ),
    ]