from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'booking_date', 'is_completed', 'number_of_persons', 'from_date', 'to_date', 'subtotal']
    list_filter = ['is_completed', 'booking_date', 'from_date', 'to_date']
    search_fields = ['user__username', 'item__title']
    ordering = ['booking_date']

    fieldsets = (
        (None, {
            'fields': ('user', 'item')
        }),
        ('Booking Details', {
            'fields': ('number_of_persons', 'from_date', 'to_date', 'subtotal')
        }),
        ('Status', {
            'fields': ('is_completed',)
        }),
    )
