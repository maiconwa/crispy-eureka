from unicodedata import category, name
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Poist(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user1 = User.objects.create_user(
            username='test_user1', password='123456789')
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1,
            status='published')
        
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        