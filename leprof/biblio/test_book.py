import unittest
import book


class Test(unittest.TestCase):
    def test_book(self):
        mybook = book.Book(ean=9782070360024, title="Le Petit Prince", authors=["Antoine de Saint-Exupéry"], publisher="Gallimard", price=6.6, lang="fr")
        self.assertEqual(mybook.ean, 9782070360024)
        self.assertEqual(mybook.title, "Le Petit Prince")
        self.assertEqual(mybook.authors, ["Antoine de Saint-Exupéry"])
        self.assertEqual(mybook.publisher, "Gallimard")
        self.assertEqual(mybook.price, 6.6)
        self.assertEqual(mybook.lang, "fr")
        mybook.title_normalized = book.Book.normalize_title(title=mybook.title)
        self.assertEqual(mybook.title_normalized, "lepetitprince")
        mybook.authors_normalized = book.Book.normalize_authors(authors=mybook.authors)
        self.assertEqual(mybook.authors_normalized, "antoinedesaintexupery")

if __name__ == '__main__':
    unittest.main()