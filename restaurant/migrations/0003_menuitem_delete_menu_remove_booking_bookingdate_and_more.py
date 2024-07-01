# Generated by Django 5.0.6 on 2024-06-30 21:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_table_alter_menu_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dish', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('inventory', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='bookingdate',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='booking',
            table=None,
        ),
    ]
