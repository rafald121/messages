import factory
from factory.django import DjangoModelFactory
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token

from messanger.models import Message


class MessageFactory(DjangoModelFactory):

    class Meta:
        model = Message


class TokenFactory(DjangoModelFactory):

    class Meta:
        model = Token


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User
