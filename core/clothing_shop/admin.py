from django.contrib import admin
from .models import Cloth, ClothBrand

@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'brand', 'price', 'stock_quantity', 'is_available') 
    
    list_filter = ('brand', 'is_available')
    
    search_fields = ('title', 'brand__name')

@admin.register(ClothBrand)
class ClothBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation_date')