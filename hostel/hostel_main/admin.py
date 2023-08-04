from django.contrib import admin
from .models import Hostel, HostelRooms


class HostelRoomsInline(admin.TabularInline):
    model = HostelRooms
    raw_id_fields = ['hostel',]


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'user', 'image', 'address', 'capacity',
        'description', 'available','created', 'updated',
    ]
    list_filter = [
        'available', 'created', 'updated',
    ]
    inlines = [HostelRoomsInline]
    