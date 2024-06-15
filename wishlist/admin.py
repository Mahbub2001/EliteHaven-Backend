from django.contrib import admin
from .models import Wishlist, WishlistItem

class WishlistItemInline(admin.TabularInline):
    model = WishlistItem
    extra = 1

class WishlistAdmin(admin.ModelAdmin):
    inlines = [WishlistItemInline]

admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(WishlistItem)
