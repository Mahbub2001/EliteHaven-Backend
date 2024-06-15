from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'availability', 'city', 'country', 'price_per_day')
    list_filter = ('availability', 'city', 'country')
    search_fields = ('title', 'description', 'city', 'country')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'map_location', 'availability', 'safety', 'weather','host','speciality')
        }),
        ('Location', {
            'fields': ('city', 'country', 'city_size')
        }),
        ('Prices', {
            'fields': ('price_per_day', 'price_per_month', 'price_6_months', 'price_1_year')
        }),
        ('Individual Expenses', {
            'fields': ('rent_individual', 'groceries_individual', 'others_individual', 'total_individual')
        }),
        ('Family Expenses', {
            'fields': ('rent_family', 'groceries_family', 'others_family', 'total_family')
        }),
        ('Pictures', {
            'fields': ('thumbnail_picture',
                        'pictures'
                        )
        }),
    )

    readonly_fields = ('pictures',)  # Assuming pictures are uploaded directly via API

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('title',)
        return self.readonly_fields
