from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'booking_date', 'is_completed']
    list_filter = ['is_completed', 'booking_date']
