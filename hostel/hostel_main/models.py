from django.db import models
from django.db.models import (
    Model, TextField, ImageField, IntegerField, CharField,
    BooleanField, ForeignKey, DateTimeField, DecimalField,
)
from django.urls import reverse


class Hostel(Model):
    name: CharField = models.CharField(max_length=100, unique=False, help_text="Enter hostel name")
    user: ForeignKey = models.ForeignKey("accounts.CustomeUser", on_delete=models.CASCADE, related_name='hostel', null=True)
    image: ImageField = models.ImageField(upload_to="hostel_img/%y/%m/%d", blank=True)
    address: CharField = models.CharField(max_length=200)
    capacity: IntegerField = models.IntegerField()
    description: TextField = models.TextField(blank=True)
    amenities: TextField = models.TextField(blank=True)
    slogan: CharField = models.CharField(max_length=100, blank=True)
    available: BooleanField = models.BooleanField(default=True)
    created: DateTimeField = models.DateTimeField(auto_now_add=True, null=True)
    updated: DateTimeField = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = [
            "-created",
        ]
        indexes = [
            models.Index(fields=['-created',])
        ]

    def __str__(self) -> str:
        """Return name and ID of hostel as a string when queried.
        """
        return F"Hostel name: {self.name} | Hostel ID: {self.id}"  # type: ignore
    
    def get_absolute_url(self) -> str:
        return reverse('hostel_main:hostel-detail-view', args=(self.id,))  # type: ignore

    
class HostelRooms(Model):
    hostel: ForeignKey = models.ForeignKey(Hostel, related_name='rooms', on_delete=models.CASCADE)
    image: ImageField = models.ImageField(upload_to="room_img/%y/%m/%d", blank=True)
    is_occupied: BooleanField = models.BooleanField(default=False)
    room_capacity: IntegerField = models.IntegerField(default=2)
    room_number: CharField = models.CharField(max_length=10, unique=False)
    description: TextField = models.TextField(blank=True)
    features: TextField = models.TextField(blank=True)
    bed_price: DecimalField = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # Unique together fields for foreignkey ref in Bookings
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['hostel', 'room_number'], name='hostel_room_no')
        ]

    def __str__(self) -> str:
        """Return room number and ID as string when queried.
        """
        return F"belongs to: {self.hostel.name} Room number: {self.room_number}"
    
    def get_absolute_url(self,) -> str:
        return reverse("hostel_main:room-detail-view", args=(self.id,)) # type: ignore
    