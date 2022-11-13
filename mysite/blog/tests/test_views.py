from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from blog.tests.test_Model_Mixin_TestCases import ModelMixinTestCase


class TestViews(ModelMixinTestCase, TestCase):
    def test_List_View_Get(self):

        response = self.client.get(self.listurl)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/list.html")

    def test_detail_View_Get(self):

        response = self.client.get(self.post_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/detail.html")
