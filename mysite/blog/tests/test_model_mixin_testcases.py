from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="karthik",
            password="123",
        )

        self.draft_post = Post.objects.create(
            title="Welcome",
            author=self.user,
            body="hi Welcome to my page",
            status="draft",
            slug="welcome",
        )
        self.published_post = Post.objects.create(
            title="Welcome back",
            author=self.user,
            body="hi whats up",
            status="published",
            slug="welcome-back",
        )
        
        
    def create_published_posts(self, count):
        posts = []
        for _ in range(count):
            post = Post.objects.create(
                title="Published2",
                author=self.user,
                body="Testing Published2",
                status="published",
                slug="published2",
            )
            posts.append(post)
        return posts
