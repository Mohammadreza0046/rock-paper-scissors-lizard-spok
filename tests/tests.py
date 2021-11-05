import unittest

from class_project import Actions, PlayAgain



class tests(unittest.TestCase):
    def test_rock_wins_over_scissors(self):
        self.assertTrue(Actions('rock'), (['scissors', 'lizard'], ['paper', 'spock']))

    def test_scissors_is_equal_scissors(self):
        self.assertTrue(Actions('scissors'), (['scissors', 'lizard'], ['paper', 'spock']))

    def test_paper_lose_to_scissors(self):
        self.assertTrue(Actions('paper'), (['paper', 'lizard'], ['rock', 'spock']))

    def test_lizard_wins_over_paper(self):
        self.assertTrue(Actions('paper'), (['spock', 'paper'], ['rock', 'scissors']))

    def test_spock_wins_over_scissors(self):
        self.assertTrue(Actions('spock'), (['rock', 'scissors'], ['paper', 'lizard']))


if __name__ == '__main__':
    unittest.main()
