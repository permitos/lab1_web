from datetime import datetime
from django.utils import timezone

from django.test import TestCase
from .models import BlogPost

class BlogPostModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        blogpost = BlogPost(public_date=timezone.now())
        self.assertIs(blogpost.was_published_recently(), True)

