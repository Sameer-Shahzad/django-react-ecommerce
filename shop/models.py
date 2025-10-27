from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    CATEGORY = (('Electronics', 'ELECTRONICS'),
                ('Clothing', 'CLOTHING'),
                ('Groceries', 'GROCERIES'),
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to="img")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=CATEGORY, max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name
    
    

def save(self, *args, **kwargs):
    if not self.id and not self.slug: 
        base_slug = slugify(self.name) 
        unique_slug = base_slug
        counter = 1
        
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{counter}' 
            counter += 1
            
        self.slug = unique_slug 
        
    super().save(*args, **kwargs)
