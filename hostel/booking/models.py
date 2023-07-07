from django.db import models
from django.db.models import (
    Model, ForeignKey, DateField
)


class Booking(Model):
    user: ForeignKey = models.ForeignKey('accounts.CustomeUser', to_field='username', on_delete=models.CASCADE, verbose_name='username') # Circular imports for custom user model.
    room: ForeignKey = models.ForeignKey('hostel_main.HostelRooms', on_delete=models.CASCADE) # Circular imports for custom user model.
    check_in_date: DateField = models.DateField()
    check_out_date: DateField = models.DateField()

    # Dunder method
    def __str__(self) -> str:
        """Return booking ID as a sting when quried
        """
        return F"Booking ID: {self.id}"
