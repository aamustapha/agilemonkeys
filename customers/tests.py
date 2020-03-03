# -*- coding: utf-8 -*-
import shutil
import tempfile

from django.test import TestCase, override_settings
from rest_framework import status
from rest_framework.test import APIClient

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestCustomer(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.sample_customer = {
            'name': 'Raliyat',
            'surname': 'Haruna'
        }
        self.addCleanup(self.remove_files)

    def remove_files(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    def create_user_and_signin(self, user=None):
        """
        Creates and sign in new user account, and also add authorization token to subsequent request headers
        """
        if user is None:
            user = {
                'email': 'abdulhakeemmustapha@gmail.com',
                'username': 'amustapha',
                'password': 'theagilemonkeys'
            }
        registration = self.client.post('/auth/users/', user)
        self.assertEqual(registration.status_code, status.HTTP_201_CREATED)
        user.pop('email')
        login = self.client.post('/auth/token/login/', user)
        self.assertEqual(login.status_code, status.HTTP_200_OK)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {login.json().get('auth_token')}")

    def test_create_customer_without_auth(self):
        """Attempts to create a customer when not authenticated, should return a 401 error."""
        request = self.client.post('/customers/', self.sample_customer)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_customer_with_auth(self):
        """Attempt to create a customer with valid credentials. Should succeed."""
        self.create_user_and_signin()
        request = self.client.post('/customers/', self.sample_customer)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_create_and_get_customer_info(self):
        """Tests that a customer is created and the owner is automatically set"""
        self.test_create_customer_with_auth()
        request = self.client.get('/customers/1/')
        expected_result = {
            'id': 1,
            'name': 'Raliyat',
            'surname': 'Haruna',
            'owner': 1,
            'modifier': 1,
            'picture': None
        }
        self.assertDictEqual(request.json(), expected_result)

    def test_create_and_update_customer(self):
        """Test that customer information is updated wih partial update."""
        self.test_create_customer_with_auth()
        update = {
            'surname': 'Mustapha'
        }
        update_request = self.client.patch('/customers/1/', update)
        self.assertEqual(update_request.status_code, status.HTTP_200_OK)
        read_request = self.client.get('/customers/1/')
        expected_result = {
            'id': 1,
            'name': 'Raliyat',
            'surname': 'Mustapha',
            'owner': 1,
            'modifier': 1,
            'picture': None
        }
        self.assertDictEqual(read_request.json(), expected_result)

    def test_create_customer_with_picture(self):
        """Test creating a customer with a picture"""
        with open('testfiles/pic-for-testing.png', 'rb') as picture:
            self.sample_customer['picture'] = picture
            self.test_create_customer_with_auth()
        read_request = self.client.get('/customers/1/')
        expected_result = {
            'id': 1,
            'name': 'Raliyat',
            'surname': 'Haruna',
            'owner': 1,
            'modifier': 1,
            'picture': 'http://testserver/media/pic-for-testing.png'
        }
        self.assertDictEqual(read_request.json(), expected_result)

    def test_check_updates_modifier(self):
        """Test that the moidifier is updated when custtomer is updated."""
        self.test_create_customer_with_auth()
        update = {
            'surname': 'Mustapha'
        }
        user2 = {
            'email': 'abdulhakeemmustapha2@gmail.com',
            'username': 'amustapha2',
            'password': 'theagilemonkeys'
        }
        self.create_user_and_signin(user=user2)
        update_request = self.client.patch('/customers/1/', update)
        self.assertEqual(update_request.status_code, status.HTTP_200_OK)
        read_request = self.client.get('/customers/1/')
        expected_result = {
            'id': 1,
            'name': 'Raliyat',
            'surname': 'Mustapha',
            'owner': 1,
            'modifier': 2,
            'picture': None
        }
        self.assertDictEqual(read_request.json(), expected_result)
