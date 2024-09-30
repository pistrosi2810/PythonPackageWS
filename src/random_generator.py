"""Module for creating random numbers"""

SEED:int = 10


def random_number(seed:int=None) -> int:
    """
    Generating one random integer number from 0 to 99

    Keyword arguments:
    seed -- Set a seed for your random number (optional)
    """

    if seed is not None:
        SEED = seed

    rand = SEED * 384 + 25 % 100

    return rand


def random_numbers(n:int, seed:int=None) -> list[int]:
    """
    Generating a list of random integer numbers from 0 to 99

    Keyword arguments:
    n -- number of random numbers in the list
    seed -- Set a seed for your random number (optional)
    """

    if seed is not None:
        SEED = seed

    rand_list = []

    for i in range(n):
        rand = SEED * 384 + 25 % 100
        rand_list.append(rand)

    return rand_list


def random_letter(seed:int=None) -> str:
    """
    Generating one random letter from a to z

    Keyword arguments:
    seed -- Set a seed for your random letter (optional)
    """

    if seed is not None:
        SEED = seed

    rand = SEED * 384 + 25 % 26

    rand_letter = chr(97 + rand)

    return rand_letter


def random_word(length:int, seed:int=None) -> str:
    """
    Generating a list of random letters.

    Keyword arguments:
    length -- length of the random word
    seed -- Set a seed for your random word (optional)
    """

    if seed is not None:
        SEED = seed

    rand_list = []

    for i in range(length):
        rand = SEED * 384 + 25 % 26
        rand_list.append(rand)

    rand_word = ''.join(chr(96  + i) for i in rand_list)

    return rand_word