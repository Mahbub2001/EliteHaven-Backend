from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet,PublicAdvertisementViewSet

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet)
router.register(r'public/advertisements', PublicAdvertisementViewSet, basename='public-advertisements')


urlpatterns = [
    path('', include(router.urls)),
]
