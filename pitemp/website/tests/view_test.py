from django.test import TestCase, Client
from website.models import *


class WebsiteTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("julien", "julien@test.fr", "password", "3 rue du moulin", "paris", "75001")
        self.user.save()

    def test_home_view(self):
        response = self.client.get('/home/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_home_authenticated_user(self):
        c = Client()
        c.login(username="julien", password="password")
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_unauthenticated_user(self):
        c = Client()
        c.login(username="julien", password="password")
        c.logout()
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_authenticated_user(self):
        c = Client()
        c.login(username="julien", password="password")
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_unauthenticated_user(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 300)
