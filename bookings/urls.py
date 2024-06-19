from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet,GetParticularUserBookings

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'user-bookings', GetParticularUserBookings, basename='particular-bookings')


urlpatterns = [
    path('', include(router.urls)),
]
