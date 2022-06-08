from django.urls import reverse
from rest_framework.test import APITestCase


class TestUser(APITestCase):
    def setUp(self):
        self.register_url = reverse('create_user')
        self.login_url = reverse('token_obtain_pair')
        self.register_data = {
            'username': 'testuser',
            'email': 'testuser4578@test.com',
            'password': 'testpassword',
        }
        self.login_data = {
            'email': 'testuser4578@test.com',
            'password': 'testpassword',
        }
        return super().setUp()


    # what is tearDown 
    def tearDown(self) -> None:
        return super().tearDown()