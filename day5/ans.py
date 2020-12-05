
with open('input.txt', 'r') as f:
    data = f.read().split()


def row_num(row):
    """
    decodes first 7 chars and returns the row number using bisection search
    """
    max_r = 127
    min_r = 0
    for char in row:
        if char == 'F':
            min_r = min_r
            max_r = (max_r + min_r) // 2 

        elif char == 'B':
            max_r = max_r
            min_r = ((max_r + min_r) // 2) + 1

    return max_r


def col_num(col):
    """
    deodes column number using bisection search 
    """
    max_c = 7
    min_c = 0
    for char in col:
        if char == 'L':
            min_c = min_c
            max_c = (max_c + min_c) // 2
        
        elif char == 'R':
            max_c = max_c
            min_c = ((max_c + min_c) // 2 ) + 1
    
    return max_c


def seat_id(row, col):
    """
    returns the formula for calculating seat id
    """
    return (row_num(row) * 8) + col_num(col)


def maxSeatID(data):
    """
    calculates all seat IDs and returns a list
    """
    seat_ids = []
    for item in data:
        seat_ids.append(seat_id(item[:7], item[7:]))
    
    return seat_ids


def missingSeatID(data):
    """
    leverages Set Subtraction to return the only
    missing seat between the full list and our calculated
    list 
    """
    seats = maxSeatID(data)
    min_id = min(seats)
    max_id = max(seats)
    check = list(range(min_id, max_id + 1))
    return set(check) - set(seats)


# part 1
print(max(maxSeatID(data)))

# part 2
print(missingSeatID(data))











        
