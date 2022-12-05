from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostListView, post_detail
from blog.tests.test_model_mixin_testcases import ModelMixinTestCase


class Testurls(ModelMixinTestCase, SimpleTestCase):
    def test_list(self):

        post_list_url = reverse("blog:post_list")
        self.assertEqual(
            (resolve(post_list_url).func.view_class), PostListView
        )

    def test_detail(self):
        post_detail_url = reverse(
            "blog:post_detail",
            args=[
                self.published_post.publish.year,
                self.published_post.publish.month,
                self.published_post.publish.day,
                self.published_post.slug,
            ],
        )
        self.assertEqual((resolve(post_detail_url).func), post_detail)
