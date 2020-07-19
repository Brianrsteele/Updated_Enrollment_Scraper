#
#   system.py
#   8/6/2019
#   Brian R Steele
#
#   Define a College or University System
#


class System:
    """
        Stores information about a college or university system.
    """
   

    def __init__(self, name, abbreviation=None, url=None):
        """
            Constructor for system objects
            :param name: String, the full name of the system
            :param abbreviation: String, the abbreviation the system uses
            :param url: String, the url for the system homepage
        """

        self.name = name
        self.abbreviation = abbreviation
        self.url = url
        
    

    def __repr__(self):
        return self.name + ", " + self.abbreviation + ", " + self.url
