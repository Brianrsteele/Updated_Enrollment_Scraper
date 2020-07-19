#
#   room.py
#   8/6/2019
#   Brian R Steele
#
#   Define a room on in a campus building
#


class Room:
    """
        Creates an object to store information about a campus room
    """

    def __init__(self, room_name, building_name = None):
        """
            Constructor for Semester class.
        :param room: String, the room number.
        :param building: Building, the building where the room is located.
        """

        self.room_name = room_name
        self.building_name = building_name

    def __repr__(self):
        return " Room Name = " + self.room_name + " Buiding Name = " + str(self.building_name)

    def __str__(self):
        return self.room_name
