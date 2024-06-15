from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Wishlist, WishlistItem
from .serializers import WishlistSerializer, WishlistItemSerializer
from hostadvertisements.models import Advertisement

class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        wishlist, created = Wishlist.objects.get_or_create(user=user)
        advertisement_id = request.data.get('advertisement_id')
        
        if not advertisement_id:
            return Response({"detail": "Advertisement ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        advertisement = Advertisement.objects.get(id=advertisement_id)
        WishlistItem.objects.create(wishlist=wishlist, advertisement=advertisement)
        
        serializer = self.get_serializer(wishlist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class WishlistItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WishlistItemSerializer

    def get_queryset(self):
        user = self.request.user
        wishlist = Wishlist.objects.get(user=user)
        return WishlistItem.objects.filter(wishlist=wishlist)

    def create(self, request, *args, **kwargs):
        user = request.user
        wishlist, created = Wishlist.objects.get_or_create(user=user)
        advertisement_id = request.data.get('advertisement_id')

        if not advertisement_id:
            return Response({"detail": "Advertisement ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        advertisement = Advertisement.objects.get(id=advertisement_id)
        wishlist_item = WishlistItem.objects.create(wishlist=wishlist, advertisement=advertisement)
        
        serializer = self.get_serializer(wishlist_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
