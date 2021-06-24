from django.shortcuts import render
from django.http import Http404

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status

from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Blog
from .serializers import BlogSerializer


class BlogListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
   
    
    def get(self,request,*args,**kwargs): 
        return self.list(self,request,*args,**kwargs)
    
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
    
    def post(self,request,*args,**kwargs): 
        return self.create(request,*args,**kwargs)
    
class BlogDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
  

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def perform_create(self,serializer):
        return serializer.save(author=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
        
class LatestBlogDetailView(APIView):
    def get(self,request,id):
        blog = Blog.get_latest_blog()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
    