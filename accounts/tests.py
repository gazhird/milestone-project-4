from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterPageTest(TestCase):
    def test_page_loads(self):
        # test register page loads
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)


class UserNotFoundTest(TestCase):
    def username_not_found(self):
        # username doesn't exist
        response = self.client.post('/accounts/login/', {
            'username': 'none',
            'password': 'testpass'
        })
        self.assertNotEqual(response.url, '/')


class WrongPasswordTest(TestCase):
    def wrong_password(self):
        # create a user
        User.objects.create_user(username="testuser", password="goodpass")
        # login with wrong password
        response = self.client.post('/accounts/login/', {
            'username': 'testuser',
            'password': 'badpass'
        })
        self.assertNotEqual(response.url, '/')

