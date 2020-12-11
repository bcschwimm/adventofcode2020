from collections import defaultdict
from itertools import combinations

with open('input.txt', 'r') as f:
    data = f.read().strip()


with open('sample.txt', 'r') as f:
    sample = f.read().strip()

sample_list = sample.split()
sample_list = [int(sample) for sample in sample_list]

volt = int(max(sample_list)) + 3

d = defaultdict(int)

for val in sample_list:
    d[volt - int(val)] += 1

print(d)
