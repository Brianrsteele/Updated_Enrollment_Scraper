#
#   meetingTime.py
#   7/14/2019
#   Brian R Steele
#
#   Define a meeting time, to be a superclass for office hours or class meeting times.
#

from timeUtilities import TimeUtilities


class MeetingTime:
    """
        holds the day of the week, start time, and end time for a meeting time, to be the superclass for class
        sessions or office hours.
    """

    def __init__(self, day_of_week, start_time, end_time):
        """
            Constructor for OfficeHour class.
        :param day_of_week: integer representing the day of the week, where Monday = 0 and Sunday = 7.
        :param start_time: String of integers representing the start time of the office hour session in 24 hour time
        format where 0900 = 9:00am and 1315 = 1:15pm.
        Enter the time as a string to preserve leading zeros.
        :param end_time: String of integers representing the end time of the office hour session in 24 hour time
        format where 0900 = 9:00am and 1315 = 1:15pm.
        Enter the time as a string to preserve leading zeros.

    """
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

        

    def __repr__(self):
        return "Day = " + str(self.day_of_week) + " Start = " + self.start_time + " End = " + self.end_time

   