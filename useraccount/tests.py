from django.test import TestCase
from useraccount.models import UserAccount

class UserModelTest(TestCase):
    def setUp(self):
        self.user = UserAccount.objects.create(
            username='john',
            email='john@example.com',
            phone_number='+123456789',
            location='123 Main St',
            password='password'
        )

    def test_user_creation(self):
      
        user = UserAccount.objects.get(username='john')

        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.phone_number, '+123456789')
        self.assertEqual(user.location, '123 Main St')
        self.assertEqual(user.password, 'password')

    def test_user_str_representation(self):
       
        self.assertEqual(str(self.user), 'john')


