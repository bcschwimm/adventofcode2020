
with open('input.txt', 'r') as f:
    data = f.read().split('\n')


def indexCalls(data: list) -> list:
    """
    takes our instruction data and returns
    the index list of the correct order
    the program should be run in
    """
    icalls = [0]
    i = 0
    
    while len(icalls) < len(data): # while loop to change index and call list values out of order
            if 'jmp' in data[i]:
                i += int(data[i][3:])
                icalls.append(i)
            else:
                i += 1
                icalls.append(i)

    return icalls


def sumData(index: list, data: list) -> int:
    """
    expects an index list with dupes
    and a data instruction list to
    calculate our sequence sum
    """
    sumval = 0
    history = []

    for i in index:
        if i in history:

            return sumval

        elif 'acc' in data[i]:
            sumval += int(data[i][3:])
            history.append(i)
        
        else:
            history.append(i)
            

# part 1
calls = indexCalls(data)
print(sumData(calls, data))

# part 2 
# TODO: change one jmp to nop or nop to jmp to terminate (run last line in code, have [:-1] == len(data)) 
