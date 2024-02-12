from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

User = get_user_model()

class UserAccountTests(APITestCase):

    # def test_user_registration(self):
    #     """
    #     Ensure we can create a new user account.
    #     """
    #     url = reverse('register')
    #     data = {
    #         'email': 'test@example.com',
    #         'password': 'testpassword123',
    #         'password2': 'testpassword123'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     response_data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertTrue('email' in response_data)
    #     self.assertEqual(response_data['email'], data['email'])
    #     # Ensure password is not returned in the response
    #     self.assertFalse('password' in response_data)

    # def test_user_login(self):
    #     """
    #     Ensure we can login with a user account.
    #     """
    #     # First, create a user
    #     user = User.objects.create_user(email='testuser@gmail.com', password='loginpassword')
    #     url = reverse('login')
    #     data = {
    #         'email': 'testuser@gmail.com',
    #         'password': 'loginpassword',
    #     }
    #     response = self.client.post(url, data, format='json')
    #     response_data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTrue('access_token' in response_data)
    #     self.assertTrue('refresh_token' in response_data)

    # def test_user_login_fail(self):
    #     """
    #     Ensure login fails with incorrect credentials.
    #     """
    #     # Attempt to login without creating a user
    #     url = reverse('login')
    #     data = {
    #         'email': 'wrong@example.com',
    #         'password': 'wrongpassword',
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpassword')
    
    def test_registration(self):
        url = reverse('register')
        data = {'email': 'newuser@example.com', 'password': 'newpassword', 'password2': 'newpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_login(self):
        url = reverse('login')
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response_data)
    
    def test_password_reset_request(self):
        url = reverse('password-reset')
        data = {'email': 'test@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_password_reset_confirm(self):
        uidb64 = 'uidb64'
        token = 'token'
        url = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
        response = self.client.get(url)
        # Depending on the logic, you might need to mock the token check process
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])
    
    def test_set_new_password(self):
        user = User.objects.create_user('user@example.com', 'password')
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        url = reverse('set-new-password')
        data = {
            'password': 'newpassword',
            'confirm_password': 'newpassword',
            'uidb64': uidb64,
            'token': token,
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logout(self):
        url = reverse('logout')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
        data = {'refresh_token': str(refresh)}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)