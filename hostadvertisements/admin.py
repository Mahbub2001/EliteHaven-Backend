from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'city', 'country', 'price_per_day', 'review_count', 
        'average_rating', 'availability'
    )
    search_fields = ('title', 'city', 'country')
    list_filter = ('availability', 'city', 'country')
    readonly_fields = ('review_count', 'average_rating', 'comments')
    
    fieldsets = (
        (None, {
            'fields': ('host', 'title', 'description', 'map_location', 'availability', 'safety', 'weather', 
                       'city', 'country', 'speciality', 'city_size', 'thumbnail_picture', 'price_per_day', 
                       'price_per_month', 'price_6_months', 'price_1_year', 'rent_individual', 'groceries_individual', 
                       'others_individual', 'total_individual', 'rent_family', 'groceries_family', 'others_family', 
                       'total_family', 'pictures')
        }),
        ('Reviews', {
            'fields': ('review_count', 'average_rating', 'comments')
        }),
    )

admin.site.register(Advertisement, AdvertisementAdmin)
