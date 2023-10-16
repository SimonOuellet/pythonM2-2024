import re
from unidecode import unidecode
class Book:
    """Book class"""
    max_length_normalization_title = 100
    max_length_normalization_authors = 100
    def __init__(self, ean: int, title: str, authors: list, publisher: str, price: float, lang: str):
        """Book Constructor
        :param ean: EAN code
        :param title: Book's Title
        :param authors: List of authors
        :param publisher: Book's Publisher
        :param price: Book's Price
        :param lang: Book's Language
        :return: Book object
        :rtype: Book
        """
        self.workid = None
        self.ean = ean
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.price = price
        self.lang = lang
        self.title_normalized = self.normalize_title()
        self.authors_normalized = self.normalize_authors()

    def __str__(self):
        """String representation of the book"""
        return f"ean:{self.ean}\ntitle:{self.title}\nauthors:{self.authors}\nprice:{self.price}"

    def set_workid(self, workid: str)->None:
        """Set workid
        :param workid: Workid
        :return: None
        """
        self.workid = workid

    def normalize_title(title: str)->str:
        """Normalize title, lower case, remove accents, remove special characters
        :return: str
        """
        if not title:
            return "notitle"
        return unidecode(re.sub(r'[^\w\s]','',title.lower()).replace(' ',''))[0:100]

    def normalize_authors(authors: list)->str:
        """Normalize authors, lower case, remove accents, remove special characters
        :return: str
        """
        if not authors:
            return "noauthors"
        authors_string = ""
        # transforme une liste d'auteurs en une chaine de caractères
        [authors_string := f"{authors_string}{author} " for author in authors]
        # normalise la chaine de caractères
        return unidecode(re.sub(r'[^\w\s]','',authors_string.lower().strip()).replace(' ',''))[0:100]