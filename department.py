#
#   department.py
#   7/13/2019
#   Brian R Steele
#
#   Define an academic department
#


class Department:
    """
        Holds information about departments, including a list of courses.
    """

    def __init__(self, abbreviation, full_name=None, url=None, school=None):
        """
            Constructor for Department class
            :param abbreviation: The department's abbreviation.
            :param: full_name: string - the full, official name of the department.
            :param: url: string - url of department information page.
            :param school: School object containing information about the college or university in which the
            department belongs.
        """
        self.abbreviation = abbreviation
        self.full_name = full_name
        self.url = url
        self.school = school

    def __repr__(self):
        department_string = 'Abbreviation = ' + self.abbreviation + ' Full Name = ' + str(self.full_name) + ' URL = ' + str(self.url) + ' School = ' + str(self.school)
        return department_string

    def __str__(self):
        department_string = self.abbreviation
        return department_string
