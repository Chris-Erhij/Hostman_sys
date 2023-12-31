# Generated by Django 4.2.3 on 2023-07-18 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_main', '0011_rename_amenities_hostelrooms_description_and_more'),
        ('booking', '0009_alter_booking_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(help_text='Format: yy/mm/dd', verbose_name='check out date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateField(help_text='Format: yy/mm/dd', verbose_name='check out date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ManyToManyField(related_name='booking', to='hostel_main.hostelrooms'),
        ),
    ]
