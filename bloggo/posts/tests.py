# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .views import about

# Create your tests here.
class AboutPage(TestCase):
    def setUp(self):
        self.c = Client()
    def testUrlResponse(self):
        response = self.c.get("/posts/about")
        self.assertEqual(response.status_code, 200,
                         "The About HTTP response should return an OK status code and not a 404")
        self.assertEqual(response.resolver_match.func, about,
                         "The URL /posts/about should resolve to the 'about' view function")
        self.assertEqual(len(response.templates), 2,
                         "The about page template should extend the base.html template")
        self.assertEqual(response.templates[0].name, "posts/base.html",
                         "The about page template should extend the base.html template")
        self.assertEqual(response.templates[1].name, "posts/about.html",
                         "The about page template should extend the base.html template")
        self.assertTrue("Bloggo is the best blog engine ever and it's gonna make me fifty trillion dollars"
                        in response.content.encode("utf-8"),
                         "The about page should contain the string "
                         "'Bloggo is the best blog engine ever and it's gonna make me fifty trillion dollars'")
        