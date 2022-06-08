from .tests_setup import TestPost
from users.models import CustomUser


class TestPostViwset(TestPost):
    post_data = {
        "title": "Test title",
        "content": "Test content",
    }


    # def test_post_list(self):
    #     response = self.client.get(self.post_list_url)
    #     print(response.data)
    #     assert response.status_code == 200

    # def test_post_create(self):
    #     res = self.client.post(self.post_list_url, self.post_data)
    #     assert res.status_code == 201

    # def test_post_create_no_data(self):
    #     res = self.client.post(self.post_list_url)
    #     assert res.status_code == 400


    def test_delete_post(self):
        res = self.client.post(self.post_list_url, self.post_data)
        post_id = res.data['id']
        res = self.client.delete(self.post_list_url + str(post_id) + '/')
        assert res.status_code == 204

    # def test_delete_randomUser_post(self):
    #     res = self.client.post(self.post_list_url, self.post_data)
    #     print('this is resposne of created post', res.data)
    #     random_user = CustomUser.objects.create_user(            
    #         username = "testuser3455",
    #         email = "test@test.com",
    #         password = "testuserlabel",
    #     )
    #     self.client.force_authenticate(user=random_user) 

    #     res = self.client.delete(self.post_list_url)
    #     print("delete status code: ", res.status_code)
    #     assert res.status_code == 403

    

    # def test_retrieve_post(self):
    #     self.client.post(self.post_list_url, self.post_data)
    #     res = self.client.get(self.post_detail_url)
    #     print(res.status_code)
    #     print(res.data)
    #     assert res.status_code == 200

    # def test_patch_post(self):
    #     # res = self.client.post(self.post_list_url, self.post_data)
    #     # post_id = res.data['id']
    #     response = self.client.put(self.post_list_url,  {'title': 'updated title'})
    #     print(response.data)
    #     print("status code is: ",response.status_code)
    #     assert response.status_code == 200
    #     assert response.data['title'] == 'updated title'