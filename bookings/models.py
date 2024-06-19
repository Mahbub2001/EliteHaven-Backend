from django.db import models
from django.conf import settings
from hostadvertisements.models import Advertisement
from datetime import date, timedelta

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    item = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    number_of_persons = models.IntegerField(default=1)
    from_date = models.DateField(default=date.today)
    to_date = models.DateField(default=date.today() + timedelta(days=1))
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Booking {self.id} by {self.user.username} for {self.item.title}'
