import pytest
import factory
from faker import Faker
from users.models import CustomUser


fake = Faker()



class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser