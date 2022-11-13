from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="karthik",
            password="123",
        )

        self.test_post_object_draft = Post.objects.create(
            title="Welcome",
            author=self.test_user,
            body="hi Welcome to my page",
            status="draft",
        )
        self.test_post_object_published = Post.objects.create(
            title="Welcome back",
            author=self.test_user,
            body="hi whats up",
            status="published",
        )
        self.test_post_object_published = Post.objects.create(
            title="Welcome back again",
            author=self.test_user,
            body="hi whats up now",
            status="published",
        )
