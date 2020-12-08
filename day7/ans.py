from collections import defaultdict

ans = []

with open('input.txt', 'r') as f:
    data = f.read().split('.')

data = [item.strip() for item in data]


def dictBuild(data):
    """
    builds a default dict with the bag and color
    as key, and types of bags it holds as value
    """
    d = defaultdict(list)

    for i in range(len(data)):
        k, v = data[i].split('contain')[0].strip(), data[i].split('contain')[-1].strip()
        k = k.strip('bags')
        d[k] = v

    return d


def holdGold(aDict):
    """
    returns a key list of bags that hold gold directly
    """
    key_list = []
    for k, v in aDict.items():
        if 'shiny gold' in v:
            key_list.append(k)

    return key_list


def iteratorDict(aDict, key_list):
    """
    takes key list and returns bags that
    hold those bags
    """
    new_list = []
    for item in key_list:
        for k, v in aDict.items():
            if item in v:
                new_list.append(k)

    return new_list


def recursion(startlist):
    """
    recursively add items to my global list
    variable 'ans' by searching the 
    dictionary for bags that can hold bags
    """
    global ans
    ans += startlist
    aDict = mydict
    if len(startlist) == 0:
        return startlist

    else:
        new = iteratorDict(aDict, startlist)
        return recursion(new)


# part 1
mydict = dictBuild(data)
hold_gold = holdGold(mydict)
recursion(hold_gold)
print(len(set(ans)))




    

