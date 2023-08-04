from django.core.validators import validate_email
from django.db import models
from django.db.models import (
    Model, DateField, BooleanField,
    CharField, EmailField, OneToOneField, DateTimeField,
    DecimalField, ForeignKey
)
from accounts.models import CustomeUser


class Booking(Model):
    BED = 'Bed'; ROOM = 'Entire room'

    ACCOMMODATAION_CHOICES = [
        (BED, 'Bed'),
        (ROOM, 'Entire Room')
    ]

    user: OneToOneField = models.OneToOneField(CustomeUser, on_delete=models.CASCADE, related_name='booking', null=True)
    room: ForeignKey = models.ForeignKey('hostel_main.HostelRooms', related_name='booking', on_delete=models.CASCADE, null=True)
    first_name: CharField = models.CharField(max_length=150, verbose_name='First name', blank=True)
    last_name: CharField = models.CharField(max_length=150, verbose_name='Last name', blank=True)
    email: EmailField = models.EmailField(blank=False, verbose_name='Email', help_text='Enter valid email', validators=[validate_email], null=True)
    check_in_date: DateField = models.DateField(help_text="Format: yy-mm-dd", verbose_name='check in date')
    check_out_date: DateField = models.DateField(help_text="Format: yy-mm-dd", verbose_name='check out date')
    booking_option: CharField = models.CharField(max_length=11, choices=ACCOMMODATAION_CHOICES, verbose_name='Accomodation type', default=ACCOMMODATAION_CHOICES[0])
    created: DateTimeField = models.DateTimeField(auto_now_add=True)
    updated: DateTimeField = models.DateTimeField(auto_now=True)
    paid: BooleanField = models.BooleanField(default=False)

    def get_amount(self) -> DecimalField:
        if self.booking_option == Booking.BED:
            price = self.room.bed_price
            
        price = self.room.bed_price * self.room.room_capacity
        return price

    # Dunder method
    def __str__(self) -> str:
        """ Return booking ID as a sting when queried
        """
        return F"Booking ID: {self.id}"  #type: ignore
