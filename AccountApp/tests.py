from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAccountTests(APITestCase):

    def test_user_registration(self):
        """
        Ensure we can create a new user account.
        """
        url = reverse('register')
        data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'password2': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('email' in response_data)
        self.assertEqual(response_data['email'], data['email'])
        # Ensure password is not returned in the response
        self.assertFalse('password' in response_data)

    def test_user_login(self):
        """
        Ensure we can login with a user account.
        """
        # First, create a user
        user = User.objects.create_user(email='testuser@gmail.com', password='loginpassword')
        url = reverse('login')
        data = {
            'email': 'testuser@gmail.com',
            'password': 'loginpassword',
        }
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response_data)
        self.assertTrue('refresh_token' in response_data)

    def test_user_login_fail(self):
        """
        Ensure login fails with incorrect credentials.
        """
        # Attempt to login without creating a user
        url = reverse('login')
        data = {
            'email': 'wrong@example.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
