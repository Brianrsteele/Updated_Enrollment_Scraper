#
#   timeUtilities.py
#   7/14/2019
#   Brian R Steele
#
#   A utility class to convert times from 24 hour to 12 hour format.
#


class TimeUtilities:

    @staticmethod
    def convert_to_12_hour(time):
        """
        Convert time to 12 hour time format, ie 0900 = 9:00am
        :return: String holding the end_time in 12 hour format
        """

        if len(time) != 4 or not (time.isnumeric()):
            raise Exception("Time must be a string with four numbers in 24 hour format, i.e. 0900.")

        if int(time) > 2400 or int(time) < 0:
            raise Exception("The value of the time must be between 0 and 2400")

        if int(time[0]) == 0:
            return time[1] + ":" + time[2:4] + " AM"
        elif int(time[0]) > 0:
            return str((int(time[0:2]) - 12)) + ":" + time[2:4] + " PM"
        else:
            raise Exception("An error occurred converting the time to the 12 hour format.")

    @staticmethod
    def convert_to_24_hour(time):
        """ 
            convert a string of time in 12 hour format to 24 hour format
            :param time: string, time in 12 hour format, ie. 12:30pm
            :return string, time in 24 hour format, ie. 1230
        """
        
        ampm = time[-2:len(time)]
        ampm = ampm.lower()
        time = time[0:-2]
        
        if ampm == "am" or ampm == "a.m.":
            time = time.split(":")
            time = "".join(time)
            if int(time) < 1000:
                time = "0" + time
            return(time)
        elif ampm == "pm" or ampm =="p.m":
            time = time.split(":")
            time = "".join(time)
            if int(time) < 1200:
                time = str(int(time) + 1200)
            return(time)
        else:
            return("Error")
            
        
        
        return(time, ampm) 
        
    
    @staticmethod
    def day_as_abbreviation(day_of_week):
        """
        Convert the day_of_week into a one or two letter abbreviation.
        :return: String with a one or two letter abbreviation for the day_of_week
        """
        if type(day_of_week) != int:
            raise Exception("Day of week must be an integer value representing the day of the week, where 0 is Monday.")

        if day_of_week < 0 or day_of_week > 6:
            raise Exception("Day of week must be between 0 and 6.")

        if day_of_week == 0:
            return "M"
        elif day_of_week == 1:
            return "T"
        elif day_of_week == 2:
            return "W"
        elif day_of_week == 3:
            return "Th"
        elif day_of_week == 4:
            return "F"
        elif day_of_week == 5:
            return "Sa"
        elif day_of_week == 6:
            return "Su"
        else:
            raise Exception("An error occurred converting day_of_week to the day abbreviation.")

    @staticmethod
    def day_as_full(day_of_week):
        """
        Convert the day_of_week into a full name for the day.
        :return: String with the full name for the day_of_week
        """
        if type(day_of_week) != int:
            raise Exception("Day of week must be an integer value representing the day of the week, where 0 is Monday.")

        if day_of_week < 0 or day_of_week > 6:
            raise Exception("Day of week must be between 0 and 6.")

        if day_of_week == 0:
            return "Monday"
        elif day_of_week == 1:
            return "Tuesday"
        elif day_of_week == 2:
            return "Wednesday"
        elif day_of_week == 3:
            return "Thursday"
        elif day_of_week == 4:
            return "Friday"
        elif day_of_week == 5:
            return "Saturday"
        elif day_of_week == 6:
            return "Sunday"
        else:
            raise Exception("An error occurred converting the day_of_week to the full day name.")
