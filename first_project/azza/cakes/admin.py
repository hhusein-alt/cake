from django.contrib import admin
from .models import Cake


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('user', 'name', 'price', 'size', 'stock', 'created_at')
      
    # Enable filtering by these fields
    list_filter = ('size', 'stock', 'created_at')
    
    # Enable search by name and ingredients
    search_fields = ('name', 'ingredients')
    
    # Default ordering in the list view
    ordering = ('-created_at', 'name')
    
    # Fields that are read-only in the admin form
    readonly_fields = ('created_at',)
    
    # Group fields in the admin form for better layout
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'price', 'size', 'ingredients', 'stock', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',),  # Collapsible section
        }),
    )
    
    # Pagination in list view
    list_per_page = 20
    
    # Optional: add a custom method for displaying price with currency
    def price_display(self, obj):
        return f"${obj.price:.2f}" if obj.price is not None else "N/A"
    price_display.short_description = 'Price'
    