import json

from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework.test import ForceAuthClientHandler
from messanger.factories import MessageFactory, TokenFactory, UserFactory
from messanger.models import Message
from rest_framework.authtoken.models import Token


class MessagesTestCase(APITestCase):

    def setUp(self):
        super().setUp()
        self.message = MessageFactory(content='Hello world')
        self.user = UserFactory(username='admin', password='adminadmin')
        self.token = TokenFactory(user=self.user)

    def test_list(self):
        result = self.client.get('/api/messages/')

        self.assertEqual(
            len(result.data), len([self.message])
        )
        self.assertEqual(result.data[0]['content'], self.message.content)

    def test_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            "content": "Hello world"
        }
        response = self.client.post('/api/messages/', data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['content'], data['content'])
        self.assertIn('views_count', response.data)
        self.assertEqual(response.data['views_count'], 0)

    def test_get(self):
        url = '/api/messages/{}/'.format(self.message.pk)
        response = self.client.get(url)

        self.assertEqual(self.message.views_count, 0)

        self.assertEqual(response.status_code, 200)

        self.message.refresh_from_db()
        self.assertEqual(self.message.views_count, 1)
        self.assertEqual(
            response.data,
            {
                'content': self.message.content, 'views_count': 1
            }
        )

    def test_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        url = '/api/messages/{}/'.format(self.message.pk)
        message_content_before = self.message.content
        response = self.client.get(url)
        self.assertEqual(response.data['content'], message_content_before)

        message_content_new = 'New content'
        self.message.content = message_content_new
        self.message.save()
        self.assertNotEqual(message_content_before, self.message.content)

        response = self.client.patch(url, data={
            'content': message_content_new
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                'content': message_content_new, 'views_count': 0
            }
        )

    def test_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        MessageFactory(content='qwe')
        self.assertEqual(Message.objects.filter(content='qwe').count(), 1)

        url = '/api/messages/{}/'.format(self.message.pk)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
