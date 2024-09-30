import unittest

from src.random_generator import RandomGenerator


class TestRandomGenerator(unittest.TestCase):

    def test_random_number(self):
        rand = RandomGenerator()

        self.assertEqual(rand.random_number(seed=10), rand.random_number(seed=10))
        self.assertIsInstance(rand.random_number(), int)

        for i in range(100):
            rand_num = rand.random_number(seed=i)
            self.assertLessEqual(rand_num, 99)
            self.assertGreaterEqual(rand_num, 0)

    def test_random_numbers(self):
        rand = RandomGenerator()

        test_numbers = rand.random_numbers(n=5, seed=28)

        self.assertEqual(test_numbers, rand.random_numbers(n=5, seed=28))
        self.assertEqual(len(test_numbers), 5)

        test_numbers = rand.random_numbers(n=100, seed=28)

        for number in test_numbers:
            self.assertLessEqual(number, 99)
            self.assertGreaterEqual(number, 0)

    def test_random_letter(self):
        rand = RandomGenerator()

        self.assertEqual(rand.random_letter(seed=10), rand.random_letter(seed=10))
        self.assertIsInstance(rand.random_letter(), str)

        letters = [chr(97 + i) for i in range(26)]

        for i in range(100):
            rand_letter = rand.random_letter(seed=i)
            self.assertIn(rand_letter, letters)

    def test_random_word(self):
        rand = RandomGenerator()

        test_word = rand.random_word(length=5, seed=28)

        self.assertEqual(test_word, rand.random_word(length=5, seed=28))
        self.assertEqual(len(test_word), 5)
        self.assertEqual(test_word, test_word.lower())

        test_word = rand.random_word(length=100, seed=28)

        letters = [chr(97 + i) for i in range(26)]

        for letter in test_word:
            self.assertIn(letter, letters)
