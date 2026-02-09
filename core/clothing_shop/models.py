from django.db import models

class ClothBrand(models.Model):
    name = models.CharField(max_length=40)
    foundation_date = models.DateField()
    bio = models.TextField(null=True , blank=True) 

    def __str__(self):
        return self.name 

class Cloth(models.Model):
    SEASON_CHOICES = (
        ("WINTER", "Winter"),
        ("SPRING", "Spring"),
        ("SUMMER", "Summer"),
        ("FALL", "Fall"),
    )    
    CATEGORY_CHOICES = (
        ("SHOES", "Shoes"),
        ("T-SHIRTS", "T-shirts"),
        ("PANTS", "Pants"),
        ("SOCKS", "Socks"),
        ("UNDERWEAR", "Underwear"),
        ("HATS", "Hats"),
    )
    
    title = models.CharField(max_length=100, default="Clothing Item") 
    cloth_color = models.CharField(max_length=30)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    stock_quantity = models.PositiveIntegerField(default=0) 
    is_available = models.BooleanField(default=True)

    brand = models.ForeignKey(
        ClothBrand,
        on_delete=models.CASCADE, 
        related_name='items',      
    )

    def __str__(self):
        return f"{self.brand.name} - {self.title}"

    def get_total_value(self):
        return self.price * self.stock_quantity

    def check_availability(self):
        if self.stock_quantity > 0:
            return True
        return False