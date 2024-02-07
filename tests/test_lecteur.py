import unittest
from src.Lecteur import Lecteur


class TestMain(unittest.TestCase):

    def test_detecter_badge(self):
        lecteur = Lecteur()
        lecteur.detecter_badge()
        self.assertTrue(lecteur.badge_detecte)

    def test_detecter_badge_wrong(self):
        lecteur = Lecteur()
        self.assertFalse(lecteur.badge_detecte)





if __name__ == '__main__':
    unittest.main()