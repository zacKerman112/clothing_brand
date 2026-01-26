from django.db import models

class ClothBrand(models.Model):
    name = models.CharField(max_length = 40)
    foundation_date = models.DateField()
    bio = models.TextField
    def __str__(self):
        return super().__str__()

class Cloth (models.Model):
    SEASON = (
        ("WINTER" , "winter"),
        ("SPRING" , "spring"),
        ("SUMMER" , "summer"),
        ("FALL" , "fall"),
    )    
    CATHEGORY = (
        ("SHOES" , "shoes"),
        ("T-SHIRTS" , "t-shirts"),
        ("PANTS" , "pants"),
        ("SOCKS" , "socks"),
        ("UNDERWEAR" , "underwear"),
        ("HATS" , "hats"),
    )
    cloth_color = models.CharField(max_length=30)
    size = models.IntegerField()
    is_avaliable = models.BooleanField()

    brand = models.ForeignKey(
        ClothBrand,
        on_delete=models.CASCADE, 
        related_name='items',      
    )



