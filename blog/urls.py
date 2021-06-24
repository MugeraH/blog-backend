from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCategoryView,LatestBlogDetailView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

path('blogs',BlogListView.as_view(),name="blogs-list"),  
path('blogs/<str:category>',BlogCategoryView.as_view(),name="blogs-category-list"),  
path('latest_blog',LatestBlogDetailView.as_view(),name="latest_blog"),  
path('blogs/<int:pk>',BlogDetailView.as_view(),name="blog-detail"),  

]

urlpatterns = format_suffix_patterns(urlpatterns)
