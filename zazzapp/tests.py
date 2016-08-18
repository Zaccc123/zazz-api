from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from zazzapp.models import User, Shout


class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('user')
        data = {'username': 'test', 'password': 'qwe123qwe123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')


class ShoutTests(APITestCase):
    def setUp(self):
        superuser = User.objects.create_superuser('test', 'test@api.com', 'testpassword')
        self.client.login(username=superuser.username, password='testpassword')

    def test_create_shout(self):
        """
        Ensure we can create a new shout object
        """
        url = reverse('shout')
        data = {'message': 'zazz api shout test'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shout.objects.count(), 1)
        self.assertEqual(Shout.objects.get().message, 'zazz api shout test')

    def test_list_shout(self):
        """
        Ensure we can create a new shout object
        """
        url = reverse('shout')
        data = {'message': 'zazz api shout test'}
        self.client.post(url, data)
        self.client.post(url, data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shout.objects.count(), 2)
