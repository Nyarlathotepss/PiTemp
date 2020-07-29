from django.test import TestCase, Client
from website.models import *


class WebsiteTest(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(username="julien", email="julien@test.fr", password="password",
                                       adress="3 rue du moulin", city="paris", postal_code="75001")

    def test_home_view(self):
        response = self.client.get('/home/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_home_authenticated_user(self):
        c = Client()
        c.login(username="julien", password="password")
        response = c.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.client.get('/authenticate/login/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_authenticated_user(self):
        c = Client()
        c.login(username="julien", password="password")
        response = c.get('/website/my_dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_my_account_authenticated_user(self):
        c = Client()
        c.login(username="julien", password="password")
        response = c.get('/authenticate/my_account/')
        self.assertEqual(response.status_code, 200)



