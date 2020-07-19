#
#   campus.py
#   8/6/2019
#   Brian R Steele
#
#   Define a campus where a building is located or a class is held.
#
import minnstateUtilities


class Campus:
    """
        Creates an object to store the name, abbreviation, street address,
        state, and zip code of a MnSCU campus.
    """

    def __init__(self, name, street_address=None,
                  city=None, state=None, postal_code=None,):
        """
            Constructor for Campus class:
            :param name: String, the name of the campus
            :param street_address: String, the street address of the campus
            :param city: String the city where the campus is located
            :param state: String, the state where the campus is located
            :param postal_code, String, the postal or zip code where the campus is located
        """

        self.name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        minnstateUtilities.populateCampusInformation(self)
    

    
    def printFormattedAddress(self):
        return self.name + "\n " \
               + self.street_address + "\n" + self.city + ", " \
               + self.state + "  " + self.postal_code        

    def __repr__(self):
        return self.name + ", " \
               + self.street_address + ", " + self.city + ", " \
               + self.state + ", " + self.postal_code

    def __str__(self):
        return self.name
