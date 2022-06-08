import pytest
from users.models import CustomUser
from pytest_factoryboy import register
from tests.factories import UserFactory


# @pytest.fixture
# def test_user_A(db):
#     user = CustomUser.objects.create_user(username='testuserA')
#     return user


# # here we are defining 
# @pytest.fixture
# def user_factory(db):
#     def create_newuser(
#         username: str,
#         # email: str,
#         # password: str = None,
#         ):
#         user = CustomUser.objects.create_user(username)  # role of CustomUser.objects
#         return user
#     return create_newuser

# @pytest.fixture
# def new_user(user_factory):
#     return user_factory('testuser')

register(UserFactory)





    




