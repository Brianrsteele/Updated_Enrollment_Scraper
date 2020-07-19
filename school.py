#
#   school.py
#   7/12/2019
#   Brian R Steele
#
#   Define a course
#
import minnstateUtilities


class School:
    """
        Stores information about a Minnesota State school, including a list of departments.
    """

    # dictionary to hold useful information about campuses
    # use to fill in missing parameters for objects on init
    

    def __init__(self, full_name, abbreviation=None, id_number=None, url=None, street_address=None, city=None,
                 state=None, postal_code=None):
        """
            Constructor for School objects
            :param full_name: string, The full, official name of the school.
            :param abbreviation: string, The abbreviation for the school, ie, "RCTC" - should be capitalized
            :param id_number, string the number used in the schedule system to identify the school.
            :param url:  string, the url of the school, include http.
            :param street_address: string, the street address of the school.
            :param city: string, the city the school is located in
            :param state: string, the two letter capitalized abbreviation of the state where the school is located.
            :param postal_code: string, zip code or postal code of the school.
        """

        self.full_name = full_name
        self.abbreviation = abbreviation
        self.id_number = id_number
        self.url = url
        self.street_address = street_address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        minnstateUtilities.populateSchoolInformation(self)

    

    def __repr__(self):
        school_string = "Abbreviation = " + self.abbreviation + " Full Name = " + self.full_name + " Id Number = " + self.id_number + " URL = " + self.url + " Street Address = " \
                        + self.street_address + " City = " + self.city + " State = " + self.state + " Postal Code = " + self.postal_code
        return school_string

    def __str__(self):
        school_string = self.abbreviation
        return school_string