from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'transaction', 'rating', 'created_at']
    list_filter = ['created_at']
