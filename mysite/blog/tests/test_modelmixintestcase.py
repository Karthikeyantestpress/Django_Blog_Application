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
        )
        self.published_post = Post.objects.create(
            title="Welcome back",
            author=self.user,
            body="hi whats up",
            status="published",
        )
