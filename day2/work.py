import itertools


with open('input.txt', 'r') as f:
    data = f.readlines()


count_list = []

for i in range(len(data)):
    count_list.append(data[i].split()[-1].count(data[i].split()[1][0]))


counter = 0

for i, val in enumerate(count_list):
    if int(data[i].split()[0].split('-')[0]) <= int(val) and int(val) <= int(data[i].split()[0].split('-')[-1]):
        counter += 1

print(counter)

clean_data = [item.strip() for item in data]

second_counter = 0

for i, val in enumerate(clean_data):
    password = clean_data[i].split(':')[-1].strip()
    index_check = int(clean_data[i].split()[0].split('-')[0])
    index_two = int(clean_data[i].split()[0].split('-')[-1])
    char = clean_data[i].split()[1][0]

    if password[index_check - 1] != char and password[index_two - 1] == char:
        second_counter += 1
    
    elif password[index_check - 1] == char and password[index_two - 1] != char:
        second_counter += 1


print(second_counter)

