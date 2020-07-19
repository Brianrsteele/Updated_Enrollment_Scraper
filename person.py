#
#   person.py
#   7/12/2019
#   Brian R Steele
#
#   Define a person to be used as a superclass for faculty, student, and staff classes
#


class Person:
    """
        Defines a person. This class is intended as a superclass for the Faculty class.
    """

    def __init__(self, first_name, last_name, telephone=None, email=None):
        """Constructor - a super-class for the Faculty class.
            :param first_name: String first name of person
            :param last_name: String last name of person
        """

        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.email = email

    def __repr__(self):
        return_string = self.first_name + " " + self.last_name
        if self.telephone is not None:
            return_string += ", " + self.telephone
        if self.email is not None:
            return_string += ", " + self.email
        return return_string
