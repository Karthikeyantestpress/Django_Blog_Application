from django.test import TestCase
from blog.models import Post
from blog.tests.test_Model_Mixin_TestCases import ModelMixinTestCase


class Test_Published_Manager(ModelMixinTestCase, TestCase):
    def test_published_should_return_only_published_posts(self):
        published_queryset = Post.published.all()
        objects_queryset_with_status_published = Post.objects.filter(
            status="published"
        )
        self.assertQuerysetEqual(
            published_queryset, objects_queryset_with_status_published
        )
