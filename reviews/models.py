from django.db import models
from django.conf import settings
from hostadvertisements.models import Advertisement
from transactions.models import Transaction

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    item = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='reviews')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.item.title}'
