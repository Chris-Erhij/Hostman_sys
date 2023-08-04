# Generated by Django 4.2.3 on 2023-07-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_main', '0010_hostel_slogan_hostelrooms_amenities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostelrooms',
            old_name='amenities',
            new_name='description',
        ),
        migrations.AddField(
            model_name='hostel',
            name='amenities',
            field=models.TextField(blank=True),
        ),
    ]