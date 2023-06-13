from django.db import models
from django.db.models import (
    Model, TextField, ImageField, IntegerField, CharField,
    EmailField, BooleanField, ForeignKey, DateTimeField
)


class Hostel(Model):
    name: CharField = models.CharField(max_length=100, unique=True, help_text="Enter hostel name")
    address: CharField = models.CharField(max_length=200)
    capacity: IntegerField = models.IntegerField()
    description: TextField = models.TextField(blank=True)
    available: BooleanField = models.BooleanField(default=True)
    created: DateTimeField = models.DateTimeField(auto_now_add=True)
    updated: DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "-created",
        ]
        indexes = [
            models.Index(fields=['-created',])
        ]

    def __str__(self) -> str:
        """Return name of hostel as a string
        """
        return F"Hostel name: {self.name}"

    
class HostelRooms(Model):
    hostel: ForeignKey = models.ForeignKey(Hostel, related_name='rooms', on_delete=models.CASCADE)
    image: ImageField = models.ImageField(upload_to="photos%y%m%d", blank=True)
    is_occupied: BooleanField = models.BooleanField(default=False)
    room_capacity: IntegerField = models.IntegerField(default=2)
    room_number: CharField = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        """Return room number as string
        """
        return F"Room number {self.room_number}"
    