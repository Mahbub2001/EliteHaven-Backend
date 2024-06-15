from django.db import models
from django.conf import settings
from hostadvertisements.models import Advertisement

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    item = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='transactions')
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return f'Transaction {self.id} by {self.user.username} for {self.item.title}'

    def save(self, *args, **kwargs):
        if self.is_successful:
            self.item.availability = False
            self.item.save()
        super().save(*args, **kwargs)
