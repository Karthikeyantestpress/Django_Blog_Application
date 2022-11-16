from django.test import TestCase
from django.urls import reverse
from blog.tests.test_model_mixin_testcases import ModelMixinTestCase


class TestViews(ModelMixinTestCase, TestCase):
    def test_templates_used_for_list_view(self):
        self.post_list_url = reverse("blog:post_list")

        response = self.client.get(self.post_list_url)
        self.assertTemplateUsed(response, "blog/post/list.html")

    def test_templates_used_for_detail_view(self):
        self.post_detail_url = reverse(
            "blog:post_detail",
            args=[
                self.published_post.publish.year,
                self.published_post.publish.month,
                self.published_post.publish.day,
                self.published_post.slug,
            ],
        )

        response = self.client.get(self.post_detail_url)

        self.assertTemplateUsed(response, "blog/post/detail.html")



