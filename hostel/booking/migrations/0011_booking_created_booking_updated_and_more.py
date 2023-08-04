# Generated by Django 4.2.3 on 2023-07-20 04:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_booking_check_in_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_option',
            field=models.CharField(choices=[('Bed', 'Bed'), ('Entire room', 'Entire Room')], default=('Bed', 'Bed'), max_length=11, verbose_name='Accomodation type'),
        ),
    ]