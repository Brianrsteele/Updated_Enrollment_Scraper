#
#   faculty.py
#   7/12/2019
#   Brian R Steele
#
#   Define a faculty member, inherits from person.py
#

from person import Person


class Faculty(Person):
    """
        Subclass of Person superclass. Creates a object representing a faculty member.
    """

    def __init__(self, first_name, last_name, extension=None, department=None, office=None, box=None,
                 telephone=None, email=None, office_hours=None):
        """
            Constructor for Faculty class.
        :param first_name: String first name of the faculty member.
        :param last_name: String last name of the faculty member.
        :param extension: String of four integers representing the faculty phone extension.
        :param department: A list holding Department object representing the various departments in which the faculty
        teaches. Remember that many adjuncts teach in multiple schools and many faculty teach in multiple departments
        in the same school.
        :param office: String holding the assigned office for the faculty member.
        :param box: String holding the mailbox name or number for the faculty member.
        :param telephone: string holding the 10 digit phone number for the faculty members office. Include the area
        code in the 000-000-0000.
        :param office_hours: List, holding a series of OfficeHour objects representing the faculty weekly office hours.
    """
        super(Faculty, self).__init__(first_name, last_name, telephone, email)
        self.extension = extension
        self.department = department
        self.office = office
        self.box = box
        self.office_hours = office_hours

    def __repr__(self):
        return self.first_name + " " + self.last_name + " Ext. = " + str(self.extension) + " Dept. = " + str(self.department) \
               + " Office = " + str(self.office) + " Box = " + str(self.box) + " Tel. = " + str(self.telephone) + " Email = " + str(self.email) + " Hours = " \
               + str(self.office_hours)

    def __str__(self):
        return self.last_name + ", " + self.first_name