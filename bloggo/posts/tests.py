# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .views import about, post_details

# Create your tests here.
class AboutPage(TestCase):
    def setUp(self):
        self.c = Client()
        self.r = self.c.get("/posts/about")
    def testUrlResponse(self):
        response = self.r
        self.assertEqual(response.status_code, 200,
                         "The About HTTP response should return an OK status code and not a 404")
        self.assertEqual(response.resolver_match.func, about,
                         "The URL /posts/about should resolve to the 'about' view function")
        self.assertEqual(len(response.templates), 2,
                         "The about page template should extend the base.html template")
        self.assertEqual(response.templates[1].name, "posts/base.html",
                         "The about page template should extend the base.html template")
        self.assertEqual(response.templates[0].name, "posts/about.html",
                         "The about page template should extend the base.html template")
        self.assertTrue(b"Bloggo is the best blog engine ever and it's gonna make me fifty trillion dollars"
                        in response.content,
                         "The about page should contain the string "
                         "'Bloggo is the best blog engine ever and it's gonna make me fifty trillion dollars'")

class PostDetailsPage(TestCase):
    def setUp(self):
        self.c = Client()
        self.r = self.c.get("/posts/details/1")
        self.r2 = self.c.get("/posts/details/2")
    def testUrlResponse(self):
        self.assertEqual(self.r.status_code, 200,
                         "The Post Details HTTP response should return an OK status code and not a 404")
        self.assertEqual(self.r2.status_code, 200,
                         "The Post Details HTTP response should return an OK status code and not a 404")
        self.assertEqual(self.r.resolver_match.func, post_details,
                         "The URL /posts/details/<pk> should resolve to the 'post_details' view function "
                         "with argument pk=<pk>")
        self.assertEqual(self.r2.resolver_match.func, post_details,
                         "The URL /posts/details/<pk> should resolve to the 'post_details' view function "
                         "with argument pk=<pk>")
    def testResponseContent(self):
        self.assertEqual(len(self.r.templates), 2,
                         "The post details template should extend the base.html template")
        self.assertEqual(self.r.templates[1].name, "posts/base.html",
                         "The post details template should extend the base.html template")
        self.assertTrue(b"Worst Day Ever" in self.r.content,
                        "The URL /posts/details/1 should contain the content of the post with pk=1 (Worst Day Ever)")
        self.assertFalse(b"Chandler" in self.r.content,
                         "The URL /posts/details/1 should not contain the content of any other posts")
        self.assertTrue(b"Chandler" in self.r2.content,
                        "The URL /posts/details/2 should contain the content of the post with pk=2 (Important Questions)")
        self.assertFalse(b"Worst Day Ever" in self.r2.content,
                         "The URL /posts/details/2 should not contain the content of any other posts")