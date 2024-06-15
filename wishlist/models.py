from django.db import models
from django.conf import settings
from hostadvertisements.models import Advertisement

class Wishlist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist item: {self.advertisement.title}"
