from itertools import combinations


with open('input.txt') as f:
    data = f.read().split()


def comboCalc(data):
    """
    returns sum combinations of a given dataset in a list
    """
    return [int(a) + int(b) for a, b in combinations(data, 2)]


def breakCypher(data, maxsize):
    """
    moving combination list to validate that my next number
    will always be a sum of the previous X values
    """
    start = 0
    for num in data[maxsize:]:
        if int(num) not in comboCalc(data[start:maxsize]):
            return num
        else:
            start += 1
            maxsize += 1


def bruteForce(data, target):
    """
    brute force looping over our data moving the starting 
    index by 1 for each pass searching for a string of
    any length that adds up to our target number
    """
    loops = 0
    x = 0
    while loops != len(data):
        ranges = []
        sumval = 0
        for val in data[x:]:
            sumval += int(val)
            ranges.append(int(val))
            if sumval == int(target):
                return ranges
        x += 1
        loops += 1


# part 1
print(breakCypher(data, 25))

# part 2
value = breakCypher(data, 25)
myrange = bruteForce(data, int(value))
print(min(myrange) + max(myrange))

