from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category

class PostTests(APITestCase):
    
    def test_view_posts(self):
        
        url = reverse('blog_api:listcreate')