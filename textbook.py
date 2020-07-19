#
#   textbook.py
#   5/19/2020
#   Brian R Steele
#
#   A class to define a textbook object.
#



class Textbook:
    """
        Defines a textbok object. 
    """

    def __init__(self, author, title, required=None, publisher=None, ISBN=None, \
                 edition=None, new_price=None, used_price=None):
        """Constructor - creates a textbook object.
            :param reqiured, string, the required status of the textbook , i.e. "EITHER/OR"
            :param title, string, the title of the textbook
            :param author, string, the last name of the author
            :param publisher, string, the name of the publisher
            :param ISBN, string, the ISBN number of the textbook
            :param edition, string, the edition of the book
            :param new_price, float, the price of a new copy of the textbook
            :param used_price, the price of a used copy of the textbook
        """
        self.required = required
        self.title = title
        self.author = author
        self.publisher = publisher
        self.ISBN = ISBN
        self.edition = edition
        self.new_price = new_price
        self.used_price = used_price
      
    def __repr__(self):
        return_string = 'Title = ' + self.title + '\n\nAuthor = ' + self.author \
                        + '\n\nPublisher = ' + str(self.publisher) + '\n\nISBN = ' \
                        + str(self.ISBN) + '\n\nEdition = ' + str(self.edition) \
                        + '\n\nNew Price = ' + str(self.new_price) + '\n\nUsed Price = ' \
                        + str(self.used_price)
        return return_string
