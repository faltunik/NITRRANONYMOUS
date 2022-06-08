# from .tests_setup import TestUser


# class TestViews(TestUser):
#     def test_register(self):
#         response = self.client.post(self.register_url, self.register_data)
#         assert response.status_code == 201
#         assert response.data['username'] == 'testuser'
#         assert response.data['email'] == 'testuser4578@test.com'
#         # assertEqual(response.data['username'], 'testuser')


#     def test_no_data_registration(self):
#         response = self.client.post(self.register_url)
#         assert response.status_code == 400


#     def test_can_login_with_data(self):
#         self.client.post(self.register_url, self.register_data)
#         response = self.client.post(self.login_url, self.login_data, format ="json")
#         assert response.status_code == 200



    # def test_login(self):
    #     self.client.post(self.register_url, self.register_data)
    #     response = self.client.post(self.login_url, self.login_data, format ="json")
    #     assert response.status_code == 400


    

    # def test_login

    # import pdb