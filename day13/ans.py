
with open('input.txt', 'r') as f:
    data = f.read().split()

timestamp = int(data[0])


def prepData(busdata: list) -> list:
    """
    returns cleaned bus id data for part 1
    """
    bus_data = busdata[1].split(',')
    return [int(elm) for elm in bus_data if elm != 'x']


def waitTime(busnum: int) -> int:
    """
    returns the wait time given a bus number
    """
    wait = 0
    while wait < timestamp:
        wait += busnum
    
    return wait - timestamp


def waitXid(buslist: list) -> int:
    """
    returns bus with least wait time * bus id
    """
    all_waits = [waitTime(bus) for bus in buslist]
    index = all_waits.index(min(all_waits))

    return min(all_waits) * buslist[index]


# part 1
busses = prepData(data)
print(waitXid(busses))



