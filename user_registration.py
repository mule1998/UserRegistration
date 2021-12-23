import re
import exception_user_registration




class UserRegistration:
    '''Here We are performing a user registration
        program in which exception and regex is used.
        For the following the test case is bieng created'''

    def first_name(self):
        return self.first_name

    def first_name(self,first_name):
        if first_name == "":
            raise exception_user_registration.ExceptionUserRegistration("First name empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$",first_name):
            self.first_name = first_name
        else:
            raise exception_user_registartion.ExceptionUserRegistration('Invalid ')

    def last_name(self):
        return self.last_name

    def last_name(self, last_name):
        if last_name == "":
            raise exception_user_registartion.ExceptionUserRegistration("Last name empty")
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", last_name):
            self.last_name = last_name
        else:
            raise exception_user_registartion.ExceptionUserRegistration('Invalid')

    def mobile(self):
 
      return self.mobile

    def mobile_no(self, mobile_no):
        if mobile_no == "":
            raise exception_user_registartion.ExceptionUserRegistration("Mobile Number empty")
        if re.fullmatch("^([91]{2}[ ])?[0-9]{10}$", mobile_no):
            self.mobile_no = mobile_no
        else:
            raise exception_user_registartion.ExceptionUserRegistration('Invalid')
