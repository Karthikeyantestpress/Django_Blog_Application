from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import post_list, post_detail
from blog.tests.test_Model_Mixin_TestCases import ModelMixinTestCase


class Testurls(ModelMixinTestCase, SimpleTestCase):
    def test_list(self):
        self.assertEqual((resolve(self.listurl).func), post_list)

    def test_detail(self):
        self.assertEqual((resolve(self.post_detail_url).func), post_detail)
