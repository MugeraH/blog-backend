from django.urls import path
from .views import BlogListView,BlogDetailView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

path('blogs',BlogListView.as_view(),name="blogs-list"),  
path('blogs/<int:pk>',BlogDetailView.as_view(),name="blog-detail"),  

]

urlpatterns = format_suffix_patterns(urlpatterns)
