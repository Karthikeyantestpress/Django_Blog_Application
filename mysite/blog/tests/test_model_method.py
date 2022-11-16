from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from blog.tests.test_model_mixin_testcases import ModelMixinTestCase


class Test_model_method(ModelMixinTestCase, TestCase):
    def test_absolute_url_in_model(self):
        self.post_detail_url = reverse(
            "blog:post_detail",
            args=[
                self.published_post.publish.year,
                self.published_post.publish.month,
                self.published_post.publish.day,
                self.published_post.slug,
            ],
        )
        self.assertEqual(
            self.post_detail_url, self.published_post.get_absolute_url()
        )
   
    def test_published_manager_should_not_have_draft_post(self):
         self.assertTrue(
            self.draft_post not in Post.published.all()
        )