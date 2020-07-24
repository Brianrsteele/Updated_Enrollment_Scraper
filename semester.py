#
#   semester.py
#   7/12/2019
#   Brian R Steele
#
#   Define an academic semester
#


class Semester:
    """
        Creates an object to store the semester, year, start_date and end_date of the semester
    """

    def __init__(self, year, semester_name, start_date=None, end_date=None):
        """
            Constructor for Semester class.
        :param year: String, the calendar year of the course.
        :param semester_name: String, the name of the semester, i.e. "Spring". No abbreviations.
        :param start_date: datetime object indicating the day classes start for the semester.
        :param end_date: datetime object indicating the day classes end for the semester.
        """

        self.year = year
        self.semester_name = semester_name
        self.start_date = start_date
        self.end_date = end_date
        self.semester_id = self.calculate_mn_state_semester_id()
        self.schools = {}

    def calculate_mn_state_semester_id(self):
        """
            Converts the calendar year and semester_name attributes to the financial
            year and semester code that Minnesota State uses in URLs, in integer format.
            :return: integer year and semester code for Minnesota State semester id.
        """

        if len(self.year) != 4 or not (self.year.isnumeric()) or not (type(self.year) == str):
            raise Exception("Year must be a string in the YYYY format.")

        self.semester_name = self.semester_name.upper()
        if self.semester_name == "FALL":
            semester_id = str(int(self.year) + 1) + '3'
        elif self.semester_name == "SPRING":
            semester_id = str(int(self.year)) + '5'
        elif self.semester_name == "SUMMER":
            semester_id = str(int(self.year) + 1) + '1'
        else:
            raise Exception("Semester_name must be FALL, SPRING, or SUMMER")
        return semester_id




    def __repr__(self):
        return "Year = " + self.year + " Name = " + self.semester_name + " Start Date = " + str(self.start_date) + " End Date " + str(self.end_date) \
               + " Semester Id = " + self.semester_id + "\n\n\tSchools ---------- " + str(self.schools)
               
    def __str__(self):
        return self.semester_name + " " + self.year
