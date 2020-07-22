#
#   textbook.py
#   5/19/2020
#   Brian R Steele
#
#   A class to define a textbook object.
#


class Textbook:
    """
        Defines a textbook object.
    """

    def __init__(self, author, title, required=None, publisher=None, isbn=None,
                 edition=None, new_price=None, used_price=None):
        """Constructor - creates a textbook object.
            :param required, string, the required status of the textbook , i.e. "EITHER/OR"
            :param title, string, the title of the textbook
            :param author, string, the last name of the author
            :param publisher, string, the name of the publisher
            :param isbn, string, the ISBN number of the textbook
            :param edition, string, the edition of the book
            :param new_price, float, the price of a new copy of the textbook
            :param used_price, the price of a used copy of the textbook
        """
        self.required = required
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.edition = edition
        self.new_price = new_price
        self.used_price = used_price
      
    def __repr__(self):
        return_string = '\n\n' + self.title + ', ' + self.author \
                        + '\nPub: ' + str(self.publisher) + ', ISBN: ' + str(self.isbn) + ', Edition: ' + str(self.edition) \
                        + '\nNew: ' + str(self.new_price) + ', Used: ' \
                        + str(self.used_price) + '\nRequired: ' + self.required
        return return_string
