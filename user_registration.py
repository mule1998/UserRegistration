import re
from exception_user_registration import ExceptionUserRegistration




class UserRegistration:
    '''
        Here We are performing a user registration
        program in which exception and regex is used.
        For the following the test case is bieng created
    '''
    def __int__(self):
        self._first_name = ""
        self._last_name = ""
        self._mobile_no = ""

    def get_first_name(self):
        return self._first_name

    def set_first_name(self,first_name):
        '''
        created function for set the first name
        '''
        if first_name == "":
            raise ExceptionUserRegistration("First Name is Empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$",first_name):
            self._first_name = first_name
        else:
            raise ExceptionUserRegistration('Invalid')

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        '''
        created function for set the last name
        '''
        if last_name == "":
            raise ExceptionUserRegistration("Last Name is Empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", last_name):
            self.last_name = last_name
        else:
            raise ExceptionUserRegistration('Invalid')

    def get_mobile_no(self):
        return self.mobile_no

    def set_mobile_no(self, mobile_no):
        '''
        created function for set the mobile number
        '''
        if mobile_no == "":
            raise ExceptionUserRegistration("Mobile Number Empty")
        if re.fullmatch("^([91]{2}[ ])?[0-9]{10}$", mobile_no):
            self.mobile_no = mobile_no
        else:
            raise ExceptionUserRegistration('Invalid')
