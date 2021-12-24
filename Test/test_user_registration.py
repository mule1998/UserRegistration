import unittest
from exception_user_registration import ExceptionUserRegistration
from user_registration import UserRegistration
class TestUserRegistration(unittest.TestCase):
    '''
    checking the user input if user input is invalid raising the exception
    '''
    def test_first_name_valid(self):
        '''
        created function for the test first name validation
        '''
        expected = 'Shubhamm'
        object_user = UserRegistration()
        object_user.set_first_name(expected)
        self.assertEqual(expected, object_user.get_first_name()) 

    def test_first_name_invalid(self):
        '''
        created function for the test first name invalidation
        '''
        expected = 'shubham'
        object_user = UserRegistration()
      
        try:
            object_user.set_first_name(expected)
        except ExceptionUserRegistration as exception:
            self.assertEqual("Invalid", exception.__str__())

    def test_first_name_empty(self):
        '''
        created function for the test first name should not be null
        '''
        expected = ''
        object_user = UserRegistration()
        try:
            object_user.set_first_name(expected)
        except ExceptionUserRegistration as exception:
            self.assertEqual("First Name is Empty", exception.__str__())

    def test_last_name_valid(self):
        '''
        created function for the test last name validation
        '''
        expected = 'Mule'
        object_user = UserRegistration()
        object_user.set_last_name(expected)
        self.assertEqual(expected, object_user.get_last_name()) 

    def test_last_name_invalid(self):
        '''
        created function for the test last name invalidation
        '''
        expected = 'mule'
        object_user = UserRegistration()
      
        try:
            object_user.set_last_name(expected)
        except ExceptionUserRegistration as exception:
            self.assertEqual("Invalid", exception.__str__())

    def test_last_name_empty(self):
        '''
        created function for the test last name should not be null
        '''
        expected = ''
        object_user = UserRegistration()
        try:
            object_user.set_last_name(expected)
        except ExceptionUserRegistration as exception:
            self.assertEqual("Last Name is Empty", exception.__str__())    
        
    def test_mobile_no_valid(self):
        expected = '9923219897'
        object_user = UserRegistration()
        object_user.set_mobile_no(expected)
        self.assertEqual(expected, object_user.get_mobile_no()) 

    def test_mobile_no_invalid(self):
        expected = '919923219897'
        object_user = UserRegistration()
        try:
            object_user.set_mobile_no(expected)
        except ExceptionUserRegistration as exception:
            self.assertEqual("Invalid", exception.__str__())

    def test_mobile_no_empty(self):
        expected = ''
        object_user = UserRegistration()
        try:
            object_user.set_mobile_no(expected)
        except ExceptionUserRegistration as exception:
            self.assertEqual("Mobile Number Empty", exception.__str__())    

if __name__ == '__main__':
    unittest.main()