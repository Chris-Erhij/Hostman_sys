from django.core.validators import validate_email
from django.db import models
from django.db.models import (
    Model, DateField, BooleanField,
    ManyToManyField, CharField, EmailField, OneToOneField
)
from accounts.models import CustomeUser


class Booking(Model):
    BED = 'bed'; ROOM = 'room'

    ACCOMMODATAION_CHOICES = [
        (BED, 'Bed'),
        (ROOM, 'Entire Room')
    ]

    user: OneToOneField = models.OneToOneField(CustomeUser, on_delete=models.CASCADE, related_name='booking', null=True)
    room: ManyToManyField = models.ManyToManyField('hostel_main.HostelRooms', related_name='booking')
    first_name: CharField = models.CharField(max_length=150, verbose_name='First name', blank=True)
    last_name: CharField = models.CharField(max_length=150, verbose_name='Last name', blank=True)
    email: EmailField = models.EmailField(blank=False, verbose_name='Email', help_text='Enter valid email', validators=[validate_email], null=True)
    check_in_date: DateField = models.DateField(help_text="Format: yy/mm/dd")
    check_out_date: DateField = models.DateField(help_text="Format: yy/mm/dd")
    booking_option: CharField = models.CharField(max_length=10, choices=ACCOMMODATAION_CHOICES, verbose_name='Accomodation type', default=ACCOMMODATAION_CHOICES[0])
    paid: BooleanField = models.BooleanField(default=False)

    # Dunder method
    def __str__(self) -> str:
        """Return booking ID as a sting when quried
        """
        return F"Booking ID: {self.id}"
