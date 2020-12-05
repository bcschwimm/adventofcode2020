import itertools
import os

os.chdir('day1')


def clean_input():
    """
    Cleans new lines from a text file
    Returns:
        List: List of Input Values
    """

    with open('input.txt', 'r') as f:
        data = f.readlines()

    data = [item.strip() for item in data]
    return data


def combos(data, combos):
    """
    Takes a list iterable and returns combinations of each

    Args:
        data Iterable: Iterable to be passed to itertools combination
    """
    return itertools.combinations(data, combos)


def sumproduct(number, combo):
    """
    takes a target sum number and number of combinations 
    and returns the numbers matching that sum, and the product

    Args:
        number int: number that you want to search to find combinations that sum to it
        combo int: number of combinations you want to build, only accepts 2 or 3.
    """
    dataset = clean_input()
    data = combos(dataset, combo)

    if combo == 2:
        for a, b in data:
            if int(a) + int(b) == number:
                print(a, b, int(a) * int(b))

    elif combo == 3:
            for a, b, c in data:
                if int(a) + int(b) + int(c) == number:
                    print(a, b, c, int(a) * int(b) * int(c))

    else:
        print('Combo must be 2 or 3')

