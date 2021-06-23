from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        read_only_fields = (
             'author',
        ),        
        fields = (
            'id',
            'title',
            'category',
            'description',
            'image_url',
            'blog_content',
            'created_at',
            'updated_at',         
        )
