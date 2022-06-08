from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import CustomUser



class TestPost(APITestCase):

    

    def setUp(self):
        self.login_url = reverse('token_obtain_pair')
        self.post_list_url = reverse('post-list')
        self.post_detail_url = reverse('post-detail', kwargs={'pk': 1})
        # self.post_create_url = reverse('post-post')

        self.user = CustomUser.objects.create_user(            
            username = "testuser",
            email = "testuser4578@test.com",
            password = "testpassword",
        )
        self.login_data = {
            'email': 'testuser4578@test.com',
            'password': 'testpassword',
        }
        

        self.token = self.client.post(self.login_url, self.login_data , format ="json")
        print(self.token.data)
        self.token = self.token.data['access']        
        self.api_authentication()
        return super().setUp()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def tearDown(self) -> None:
        return super().tearDown()
