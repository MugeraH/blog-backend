from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Blog(models.Model):
    LIFE = 'life'
    BUSINESS = 'business'
    TRAVEL = 'travel'
    RANDOM_THOUGHTS = 'random_thoughts'
    CARRER = 'carrer'
    ENTERTAINMENT = 'entertainment'
    
    
    CHOICES_CATEGORY = {
        (LIFE,'Life'),
        (BUSINESS,'Business'),
        (RANDOM_THOUGHTS,'Random_thoughts'),
        (TRAVEL,'Travel'),
        (CARRER,'Carrer'),
        (ENTERTAINMENT,'Entertainment')
    }   
    
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=25 ,choices=CHOICES_CATEGORY, default=LIFE)
    description = models.TextField(null=True)
    image = CloudinaryField('image',null=True)
    author = models.ForeignKey(User,related_name='leads',on_delete=models.CASCADE)
    blog = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
