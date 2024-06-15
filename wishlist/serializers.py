from rest_framework import serializers
from .models import Wishlist, WishlistItem
from hostadvertisements.serializers import AdvertisementSerializer

class WishlistItemSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer()

    class Meta:
        model = WishlistItem
        fields = ['id', 'advertisement']

class WishlistSerializer(serializers.ModelSerializer):
    items = WishlistItemSerializer(many=True, required=False)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'items']
