from itertools import chain


with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')
    
groups = [item.split() for item in data]


def uniqueYes(data):
    """
    Takes a list of groups, flattens
    the list, sums and returns number of
    unique yes question answers per group
    """
    ans = 0
    for group in data:
        ans += len(set(chain.from_iterable(group)))
    
    return ans


def yesIntersect(data):
    """
    creates a list of sets and adds
    only intersecting elements to the total
    """
    new = []
    common = 0
    for group in data:
        new.append(set(group))
    
    for row in new:
        inter = []
        for elm in row:
            inter.append(set(elm))
        
        common += len(set.intersection(*inter)) # * for unpacking x amount of elements to pass to intersection
    
    return common

# part 1
print(uniqueYes(groups))

# part 2
print(yesIntersect(groups))
