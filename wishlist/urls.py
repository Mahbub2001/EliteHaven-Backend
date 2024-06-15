from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WishlistViewSet, WishlistItemViewSet

router = DefaultRouter()
router.register(r'wishlist', WishlistViewSet, basename='wishlist')
# router.register(r'wishlist-items', WishlistItemViewSet, basename='wishlistitem')

urlpatterns = [
    path('', include(router.urls)),
]
