import re


with open('batch.txt', 'r') as f:
    clean = f.read()

cleanpass = [item.replace('\n', ' ') for item in clean.split('\n\n')] 
# strip only removes from beginning or end, use replace for mid string \n cleaning

def scanPass(data):
    accepted = 0
    valid = 'eyr iyr byr ecl pid hcl hgt cid'.split()
    valid2 = 'eyr iyr byr ecl pid hcl hgt'.split()
    for i in range(len(data)):
        if all(x in data[i] for x in valid):
            accepted += 1
        elif all(x in data[i] for x in valid2):
            accepted += 1
        else:
            pass
    
    return accepted

# part 1

def passedPass(data):
    accepted = 0
    passed = []
    valid = 'eyr iyr byr ecl pid hcl hgt cid'.split()
    valid2 = 'eyr iyr byr ecl pid hcl hgt'.split()
    for i in range(len(data)):
        if all(x in data[i] for x in valid):
            accepted += 1
            passed.append(data[i])
        elif all(x in data[i] for x in valid2):
            accepted += 1
            passed.append(data[i])
        else:
            pass
    
    return passed

# soultion 1
print(scanPass(cleanpass))


# building dictionary for membership testing using dict comp
aDict = {item.split(':')[0]: item.split(':')[-1] for item in cleanpass[0].split()}
# print(aDict)

final_clean = passedPass(cleanpass)

def condition_check(aDict):
    true_count = 0
    if 2020 <= int(aDict['eyr']) <= 2030:
        true_count += 1

    if 2010 <= int(aDict['iyr']) <= 2020:
        true_count += 1

    if 1920 <= int(aDict['byr']) <= 2002:
        true_count += 1

    if aDict['ecl'] in 'amb blu brn gry grn hzl oth'.split():
        true_count += 1

    if len(aDict['pid']) == 9:
        true_count += 1

    pattern = r'#[^g-z]{6}'
    if re.search(pattern, aDict['hcl']):
        true_count += 1

    try:
        if 'cm' in aDict['hgt'] and 150 <= int(aDict['hgt'][0:3]) <= 193:
            true_count += 1

    except ValueError:
        pass

    try:
        if 'in' in aDict['hgt'] and 59 <= int(aDict['hgt'][0:2]) <= 76:
            true_count += 1

    except ValueError:
        pass

    return true_count

passing = 0

for i in range(len(final_clean)):
    aDict = {item.split(':')[0]: item.split(':')[-1] for item in final_clean[i].split()}
    if condition_check(aDict) >= 7:
        passing += 1


# problem 2
print(passing)
