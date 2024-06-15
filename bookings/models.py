from django.db import models
from django.conf import settings
from hostadvertisements.models import Advertisement

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    item = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Booking {self.id} by {self.user.username} for {self.item.title}'
