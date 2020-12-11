from collections import defaultdict
from itertools import tee


with open('input.txt', 'r') as f:
    data = f.read().split()


def dataPrep(mydata: list) -> list:
    """
    converting to int, sorting and appending 
    our 0 starting volt value and 
    max volt value (max + 3) to our list
    """
    mylist = [int(elm) for elm in mydata]

    volt = int(max(mylist)) + 3
    start = 0

    mylist.extend([volt, start])
    mylist.sort()

    return mylist


def differences(data: list) -> list:
    """
    turns your list into two iterables, 
    moves index up for one list and 
    returns the differences between each element
    """
    differences = []
    iterable, copy = tee(data)
    next(copy) # adjusts copy of my iterable up 1 element
    for x, y in zip(iterable, copy):
        differences.append(abs(x - y))

    return differences


def dictCount(aList: list) -> dict:
    """
    takes a list and returns the count of each
    value in that list via defaultdict
    """
    d = defaultdict(int)
    for elm in aList:
        d[elm] += 1

    return d


# part 1
cleanList = dataPrep(data)
difference = differences(cleanList)
counts = dictCount(difference)
print(counts[1] * counts[3])




