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
    # image = CloudinaryField('image',null=True)
    image_url = models.URLField(null=True)
    author = models.ForeignKey(User,related_name='blogs',on_delete=models.CASCADE)
    blog_content = models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save_blog(self):
        self.save()

    def delete_blog(self):
        self.delete()
        
    @classmethod
    def get_latest_blog(cls):
        blog = Blog.objects.all().order_by('id').last()
        return blog
    
    @classmethod
    def get_blog_by_id(cls,id):
        blog = Blog.objects.filter(pk=id)
        return blog
    
    @classmethod
    def filter_blog_by_category(cls,category):
        return cls.objects.filter(category__icontains=category).all()
    
    
    def __str__(self):
        return self.title
    
