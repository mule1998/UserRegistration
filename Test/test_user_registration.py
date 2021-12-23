import unittest
import exception_user_registration
from user_registration import UserRegistration


class TestUserRegistration(unittest.TestCase):
    def test_first_name_valid(self):
        expected = 'Shubhamm'
        object_user = UserRegistration()
        object_user.first_name(expected)
        self.assertEqual(expected, object_user.first_name())

    def test_first_name_invalid(self):
        expected = 'shubham'
        object_user = UserRegistration()
      
        try:
            object_user.first_name(expected)
        except exception_user_registration.ExceptionUserRegistration as exception:
            self.assertEqual("Invalid", exception.__str__())

    def test_first_name_empty(self):
        expected = ''
        object_user = UserRegistration()
        try:
            object_user.first_name(expected)
        except exception_user_registration.ExceptionUserRegistration as exception:
            self.assertEqual("First Name is Empty", exception.__str__())

if __name__ == '__main__':
     unittest.main()