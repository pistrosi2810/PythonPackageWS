import unittest

from src.random_generator import (
    random_letter,
    random_number,
    random_numbers,
    random_word,
)


class TestRandomGenerator(unittest.TestCase):

    def test_random_number(self):

        self.assertEqual(random_number(seed=10), random_number(seed=10))
        self.assertIsInstance(random_number(), int)

        for i in range(100):
            rand_num = random_number(seed=i)
            self.assertLessEqual(rand_num, 99)
            self.assertGreaterEqual(rand_num, 0)

    def test_random_numbers(self):

        test_numbers = random_numbers(n=5, seed=28)

        self.assertEqual(test_numbers, random_numbers(n=5, seed=28))
        self.assertEqual(len(test_numbers), 5)

        test_numbers = random_numbers(n=100, seed=28)

        for number in test_numbers:
            self.assertLessEqual(number, 99)
            self.assertGreaterEqual(number, 0)

    def test_random_letter(self):
        self.assertEqual(random_letter(seed=10), random_letter(seed=10))
        self.assertIsInstance(random_letter(), str)

        letters = ['a' + i for i in range(26)]

        for i in range(100):
            rand_letter = random_letter(seed=i)
            self.assertIn(rand_letter, letters)

    def test_random_word(self):

        test_word = random_word(n=5, seed=28)

        self.assertEqual(test_word, random_word(n=5, seed=28))
        self.assertEqual(len(test_word), 5)
        self.assertEqual(test_word, test_word.lower())

        test_word = random_word(n=100, seed=28)

        letters = ['a' + i for i in range(26)]

        for letter in test_word:
            self.assertIn(letter, letters)
