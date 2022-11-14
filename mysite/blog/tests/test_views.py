from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from blog.tests.test_modelmixintestcase  import ModelMixinTestCase


class TestViews(ModelMixinTestCase, TestCase):
    def test_templates_used_for_list_view(self):

        response = self.client.get(self.post_list_url)
        self.assertTemplateUsed(response, "blog/post/list.html")

    def test_templates_used_for_detail_view(self):

        response = self.client.get(self.post_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/detail.html")
