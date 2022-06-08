import pytest

from django.conf import settings
from users.models import CustomUser


# @pytest.mark.django_db
# def test_user():
#     CustomUser.objects.create_user(username='testuser', email="test2345567user@test.com")
#     assert CustomUser.objects.all().count() == 1


# @pytest.fixture
# def test_user_A(db):
#     user = CustomUser.objects.create_user(username='testuserA')
#     return user


# def test_user_password(test_user_A):
#     test_user_A.set_password('testuserA')
#     print(test_user_A.password)
#     print(test_user_A.username)
#     assert test_user_A.check_password('testu') is True

# def test_newuser(new_user):
#     print(new_user.username)
#     print(new_user.email)
#     assert new_user.username == 'testuser'
#     assert new_user.email == ''

@pytest.mark.django_db
def test_user_factory(user_factory):
    user = user_factory.create()
    print(user.username)
    assert True



