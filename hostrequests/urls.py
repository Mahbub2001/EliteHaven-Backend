from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HostRequestViewSet, HostViewSet, AdminActionView

router = DefaultRouter()
router.register(r'hostreq', HostRequestViewSet)
router.register(r'hosts', HostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin-action/', AdminActionView.as_view(), name='admin_action'),
]
