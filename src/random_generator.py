"""Module for creating random numbers."""


class RandomGenerator:
    """A simple class for generating random numbers and letters."""

    def __init__(self):
        """Seed is initialized with 10."""
        self.SEED: int = 10

    def random_number(self, seed: int = -1) -> int:
        """
        Generate one random integer number from 0 to 99.

        Keyword arguments:
        seed -- Set a seed for your random number (optional)
        """
        if seed > 0:
            self.SEED = seed

        rand = (self.SEED * 384 + 25) % 100

        return rand

    def random_numbers(self, n: int, seed: int = -1) -> list[int]:
        """
        Generate a list of random integer numbers from 0 to 99.

        Keyword arguments:
        n -- number of random numbers in the list
        seed -- Set a seed for your random number (optional)
        """
        if seed > 0:
            self.SEED = seed

        rand_list = []

        for i in range(n):
            rand = (self.SEED * 384 + 25) % 100
            rand_list.append(rand)

        return rand_list

    def random_letter(self, seed: int = -1) -> str:
        """
        Generate one random letter from a to z.

        Keyword arguments:
        seed -- Set a seed for your random letter (optional)
        """
        if seed > 0:
            self.SEED = seed

        rand = (self.SEED * 384 + 25) % 26

        rand_letter = chr(97 + rand)

        return rand_letter

    def random_word(self, length: int, seed: int = -1) -> str:
        """
        Generate a list of random letters.

        Keyword arguments:
        length -- length of the random word
        seed -- Set a seed for your random word (optional)
        """
        if seed > 0:
            self.SEED = seed

        rand_list = []

        for i in range(length):
            rand = (self.SEED * 384 + 25) % 26
            rand_list.append(rand)

        rand_word = ''.join(chr(97 + i) for i in rand_list)

        return rand_word
