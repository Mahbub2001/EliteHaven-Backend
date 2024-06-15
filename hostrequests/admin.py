# admin.py
from django.contrib import admin
from .models import HostRequest, Host

@admin.register(HostRequest)
class HostRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_status', 'request_date', 'admin', 'response_date', 'property_address', 'property_type', 'property_name',)
    search_fields = ('user__username', 'property_name', 'property_address')
    list_filter = ('request_status', 'request_date')

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'email', 'host_approval_status', 'property_address', 'property_type', 'property_name',)
    search_fields = ('person__username', 'property_name', 'property_address')
    list_filter = ('host_approval_status',)
