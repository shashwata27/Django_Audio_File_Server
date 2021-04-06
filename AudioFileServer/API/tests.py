from django.test import TestCase
from django.contrib.auth import get_user_model
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
    