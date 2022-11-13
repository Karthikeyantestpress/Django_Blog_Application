from django.test import SimpleTestCase
from blog.forms import EmailPostForm


class TestForms(SimpleTestCase):
    def test_Email_form_valid_data(self):
        form = EmailPostForm(
            data={
                "name": "karthik",
                "email": "karthiktest51@gmail.com",
                "to": "Karthikeyankarthik896@gmail.com",
                "comments": "Good Posts",
            }
        )

        self.assertTrue(form.is_valid())

    def test_Email_form_invalid_data(self):
        form = EmailPostForm(
            data={
                "name": "karthik",
                "email": 123,
                "to": "Karthikeyankarthik896@gmail.com",
                "comments": "Good Posts",
            }
        )

        self.assertFalse(form.is_valid())

    def test_Email_form_no_data(self):
        form = EmailPostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
