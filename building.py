#
#   building.py
#   8/6/2019
#   Brian R Steele
#
#   Define a building where a room is located or a class is held.
#


class Building:
    """
        Creates an object to store the school, name, abbreviation, latitude, and longitude of a campus building.
    """

    def __init__(self, name, abbreviation=None, school=None, campus=None, latitude=None, longitude=None):
        """
            Constructor for Campus class:
            :param name: String, the name of the campus
            :param abbreviation: String, the abbreviation of the campus name
            :param school: School, School object that holds information about the school where the building is
            located.
            :param campus: Campus object that holds information about the campus on which the building is located
            :param latitude, String the latitude of the campus
            :param longitude, String the longitude of the campus
        """

        self.name = name
        self.abbreviation = abbreviation
        self.school = school
        self.campus = campus
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return self.name + ", " + self.abbreviation + ", " \
               + self.school + ", " + self.campus + ", " + self.latitude + ", " \
               + self.longitude

    def __str__(self):
        return self.name
