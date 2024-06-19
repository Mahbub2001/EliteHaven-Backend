from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'item', 'booking_date', 'is_completed', 'number_of_persons', 'from_date', 'to_date', 'subtotal']
        read_only_fields = ['id', 'user', 'booking_date', 'is_completed']
