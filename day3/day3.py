
with open('input.txt', 'r') as f:
    data = f.readlines()

data = [item.strip() for item in data]
data = [item * 1000 for item in data] # thanks andrew


def slopes(data, right):
    """
    Assumes you are only taking one step down
    """
    index = 0
    count = 0
    tree = '#'
    for row in data:
        if row[index] == tree:
            count += 1
            index += right
        else:
            index += right

    return count

# part 1
print(slopes(data, 3))

# part 2
s1, s2, s3, s4, s5 = slopes(data, 1), slopes(data, 3), slopes(data, 5), slopes(data, 7), slopes(data[::2], 1)

print(s1 * s2 * s3 * s4 * s5)
