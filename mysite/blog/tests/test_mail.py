from django.test import TestCase
from blog.tests.test_model_mixin_testcases import ModelMixinTestCase
from django.urls import reverse


class TestEmail(ModelMixinTestCase, TestCase):
    def test_post_share_template_used(self):
        post_share_url = reverse(
            "blog:post_share", args=[self.published_post.id]
        )
        response = self.client.get(post_share_url)

        self.assertTemplateUsed(response, "blog/post/share.html")
