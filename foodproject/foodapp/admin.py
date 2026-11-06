from django.contrib import admin
from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'food_name',
        'hotel_name',
        'category',
        'price',
        'is_available',
    )

    search_fields = ('food_name', 'hotel_name', 'category')
    list_filter = ('category', 'is_available')