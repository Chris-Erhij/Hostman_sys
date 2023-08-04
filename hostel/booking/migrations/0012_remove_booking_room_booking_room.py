# Generated by Django 4.2.3 on 2023-07-20 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("hostel_main", "0012_rename_price_hostelrooms_bed_price_and_more"),
        ("booking", "0011_booking_created_booking_updated_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="room",
        ),
        migrations.AddField(
            model_name="booking",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="booking",
                to="hostel_main.hostelrooms",
            ),
        ),
    ]