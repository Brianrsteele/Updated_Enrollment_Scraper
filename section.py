#
#   section.py
#   7/13/2019
#   Brian R Steele
#
#   contain information about a section
#


class Section:
    """
        Holds information about a section of a course - based on the information stored in the class schedule.

    """

    def __init__(self, semester, course, section_number, meeting_times=None, start_date=None, end_date=None,
                 status=None, instructor=None, delivery_method=None, offered_through=None,
                 location=None, size=None, enrolled=None, full_refund_date=None, last_add_date=None,
                 last_drop_date=None, last_withdraw_date=None, resident_tuition=None,
                 nonresident_tuition=None, approximate_course_fees=None, textbooks=None):
        """
        Constructor for section objects.
        :param semester: A semester object.
        :param course: A course object.
        :param section_number: a string, to retain leading zeros, ie "01"
        :param meeting_times: List of MeetingTime objects holding the meeting time information about the course
        :param start_date: a DateTime object containing the starting date of the course, which might be different
        than the starting date of the semester.
        :param end_date: a DateTime object storing the ending date of the course, which might be different than the
        ending date of the semester.
        :param status: string of the current course status, should be "Open", "Full", or "Cancelled"
        :param instructor: list of instructor objects representing the instructors teaching the course".
        :param delivery_method: string: the delivery_method as listed on class schedule.
        :param offered_through: School, the campus listed as offering the course
        :param location: String, the location of the class
        :param size: int, the number of possible student who could enroll in the course.
        :param enrolled: int, the number of students actually enrolled in the course.
        :param full_refund_date: datetime object indicating the date a student may withdraw from the course for a full
        refund.
        :param last_add_date: datetime object indicating the last date a student can add the course.
        :param last_drop_date: datetime object indicating the last date a student can drop the course.
        :param last_withdraw_date: datetime object indicating the last date a student can withdraw from the class.
        :param resident_tuition: float,  store tuition cost for in state residents
        :param nonresident_tuition: float, tuition costs for out of state students
        :param approximate_course_fees: float, pennies to store the cost of course fees for the section.
        :param textbooks: a list of textbook object containing information about the section's textbooks.
        :return: None
        """

        self.semester = semester
        self.course = course
        self.section_number = section_number
        self.meeting_times = meeting_times
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.instructor = instructor
        self.delivery_method = delivery_method
        self.offered_through = offered_through
        self.location = location
        self.size = size
        self.enrolled = enrolled
        self.full_refund_date = full_refund_date
        self.last_add_date = last_add_date
        self.last_drop_date = last_drop_date
        self.last_withdraw_date = last_withdraw_date
        self.resident_tuition = resident_tuition
        self.nonresident_tuition = nonresident_tuition
        self.approximate_course_fees = approximate_course_fees
        self.textbooks = textbooks

    def __repr__(self):
        return "\n\nSemester = " + str(self.semester) + " \n\nCourse = " + str(self.course) + " \n\nSection Num = " + str(self.section_number) + " \n\nStart Date = " \
               + str(self.start_date) + " \n\nEnd Date = " + str(self.end_date) + " \n\nMeeting Times = " + str(self.meeting_times) \
               + "\n\nStatus = " + self.status + "\n\nInstructor = " + str(self.instructor) \
               + "\n\nDelivery = " + self.delivery_method + "\n\nSchool = " + str(self.offered_through) \
                + "\n\nLocation = " + self.location + "\n\nSize = " + self.size + "\n\nEnrollment = "+ self.enrolled \
                + "\n\nFull Refund Date = " + str(self.full_refund_date) + "\n\nLast Add Date = " \
                + str(self.last_add_date) + "\n\nLast Drop Date = " + str(self.last_drop_date) \
                + "\n\nLast Withdraw Date = " + str(self.last_withdraw_date) + "\n\nNon-Resident Tuition = " \
                + str(self.nonresident_tuition) + "\n\nResident Tuition = " + str(self.resident_tuition) \
                + "\n\nFees = " + str(self.approximate_course_fees) + "\n\nTextbooks =" + str(self.textbooks)