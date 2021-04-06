from django.test import TestCase
from django.contrib.auth import get_user_model
from AudioFileServer import settings
# Create your tests here.

User=get_user_model()

class User_test_Case(TestCase):
    def setUp(self): # Python's builtin unittest
        user_a = User(username='admin', email='')
        user_a_pw = 'admin'
        self.user_a_pw = user_a_pw
        user_a.is_superuser = True
        user_a.is_staff = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
    
    def test_userexists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1) # ==
        self.assertNotEqual(user_count, 0) # !=

   
    def test_userpassword(self):
        user_a = User.objects.get(username="admin")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )
    
    def test_login_url(self):
        # login_url = "/login/"
        # self.assertEqual(settings.LOGIN_URL, login_url)
        login_url = settings.LOGIN_URL
        # python requests - manage.py runserver
        # self.client.get, self.client.post
        # response = self.client.post(url, {}, follow=True)
        data = {"username": "admin", "password": "admin"}
        response = self.client.post(login_url, data, follow=True)
        # print(dir(response))
        # print(response.request)
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)