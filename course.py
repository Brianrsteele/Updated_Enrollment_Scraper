#
#   course.py
#   7/12/2019
#   Brian R Steele
#
#   Define a course
#


class Course:
    """
        Superclass to hold basic course information and contains a list of CourseListing objects.
        Course objects will be aggregated into a courses_list in the Department class.
    """

    def __init__(self, number, title=None, description=None, credit_hours=None, course_level=None,
                 mntc_goals=None, pre_reqs=None):
        """
        Constructor for Course objects.
        :param department: A Department object
        :param number: String, course number, i.e. "1184"
        :param title: String of course title, i.e. "Photography I".
        :param description: catalog or CCO course description".
        :param credit_hours: int: number of credit hours the course is worth".
        :param course_level: string: should be "Undergraduate" or "Graduate".
        :param mntc_goals: list of MntcGoal objects: a list of objects representing MnTC goals".
        :return: None
        """
        self.number = number
        self.title = title
        self.description = description
        self.credit_hours = credit_hours
        self.course_level = course_level
        self.mntc_goals = mntc_goals
        self.pre_reqs = pre_reqs
        self.sections = {}

    def __repr__(self):
        """
            Create a human readable output for the course.
        """
        course_string = "Course Number: " \
                        + self.number + " Title:" + self.title + " Credit Hours = " \
                        + self.credit_hours + ", Course Level: " + self.course_level \
                        + " , MnTC Goals: " + str(self.mntc_goals) + " Pre-Reqs: " \
                        + self.pre_reqs + " Description: " + self.description \
                        + str(self.sections)

        return course_string