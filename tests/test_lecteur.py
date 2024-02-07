import unittest
from src.Lecteur import Lecteur


class TestMain(unittest.TestCase):

    def test_hello_morning(self):
        lecteur = Lecteur()
        lecteur.detecter_badge()
        self.assertTrue(lecteur.badge_detecte)




if __name__ == '__main__':
    unittest.main()