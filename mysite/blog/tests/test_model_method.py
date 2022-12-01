from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from blog.tests.test_model_mixin_testcases import ModelMixinTestCase


class Test_model_method(ModelMixinTestCase, TestCase):
    def test_absolute_url_in_model(self):
        post_detail_url = reverse(
            "blog:post_detail",
            args=[
                self.published_post.publish.year,
                self.published_post.publish.month,
                self.published_post.publish.day,
                self.published_post.slug,
            ],
        )
        self.assertEqual(
            post_detail_url, self.published_post.get_absolute_url()
        )

    def test_published_manager_should_not_have_draft_post(self):
        self.assertTrue(self.draft_post not in Post.published.all())

    def test_get_top_four_similar_posts_returns_empty_for_post_without_tag(
        self,
    ):
        self.assertQuerysetEqual(
            Post.objects.none(),
            self.published_post.get_top_four_similar_posts(),
        )

    def test_get_top_four_similar_posts_returns_similar_posts_for_post_with_tag(
        self,
    ):

        posts = self.create_published_posts(count=2)
        first_post = posts[0]
        first_post.tags.add("test")
        second_post = posts[1]
        second_post.tags.add("test")

        self.assertTrue(second_post in first_post.get_top_four_similar_posts())
