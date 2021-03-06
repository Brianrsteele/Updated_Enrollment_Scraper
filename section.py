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

    def __init__(self, section_number, meeting_times=None, start_date=None, end_date=None,
                 status=None, instructor=None, delivery_method=None,
                 location=None, size=None, enrolled=None, full_refund_date=None, last_add_date=None,
                 last_drop_date=None, last_withdraw_date=None, resident_tuition=None,
                 nonresident_tuition=None, approximate_course_fees=None, textbooks=None):
        """
        Constructor for section objects.
        :param section_number: a string, to retain leading zeros, ie "01"
        :param meeting_times: List of MeetingTime objects holding the meeting time information about the course
        :param start_date: a DateTime object containing the starting date of the course, which might be different
        than the starting date of the semester.
        :param end_date: a DateTime object storing the ending date of the course, which might be different than the
        ending date of the semester.
        :param status: string of the current course status, should be "Open", "Full", or "Cancelled"
        :param instructor: list of instructor objects representing the instructors teaching the course".
        :param delivery_method: string: the delivery_method as listed on class schedule.
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

        self.section_number = section_number
        self.meeting_times = meeting_times
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.instructor = instructor
        self.delivery_method = delivery_method
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
        return "\n\n\t\t\t\t\t\tSection ----------------" \
                +  "\n\n\t\t\t\t\t\t\tSection Num: " + str(self.section_number) + ", Status: " + self.status \
                + " Start Date: " + str(self.start_date) + ", End Date: " + str(self.end_date) \
                + " Meeting Times:" + str(self.meeting_times) \
                + " Instructor = " + str(self.instructor) \
               + " Delivery: " + self.delivery_method  \
                + ", Location: " + self.location + "Size:" + self.size + ", Enrollment = "+ self.enrolled \
                + "Dates: " + "Full Refund: " + str(self.full_refund_date) + " Last Add: " \
                + str(self.last_add_date) + "Last Drop Date: " + str(self.last_drop_date) \
                + " Last Withdraw: " + str(self.last_withdraw_date) \
                + ' Tuition: ' + "Non-Resident: $" \
                + str(self.nonresident_tuition) + ", Resident: $" + str(self.resident_tuition) \
                + ", Fees: $" + str(self.approximate_course_fees)  + self.print_textbooks()

    def print_textbooks(self):
        return_string = ''
        for book in self.textbooks:
            return_string = return_string + str(book)
        return return_string