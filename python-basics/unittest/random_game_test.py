import unittest
import random_game

class TestGame(unittest.TestCase):
    def test_input(self):
        # please note in the video, I had the parameters flipped it should be the "guess" parameter 1st and "answer" parameter 2nd
        result = random_game.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = random_game.run_guess(0, 1)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = random_game.run_guess(5,11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = random_game.run_guess(5, '11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()