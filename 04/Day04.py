import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1 = 0

def real_rooms(data):
    global PART_1
    for line in data:
        name, id, checksum = parse_input(line)
        if is_real_room(name, checksum):
            PART_1 += int(id)



def parse_input(line):
    name, right = line.rsplit('-', 1)
    id, checksum = right.strip(']').split('[')
    return name, id, checksum

def is_real_room(name, checksum):
    print("new line")
    d = defaultdict(int)
    x = defaultdict(list)
    for char in name:
        if char.isalpha():
            d[char] += 1
    for key, value in d.items():
        x[value] += key

    sorted_x = sorted(x.items(), key=lambda item: item[0], reverse=True)
    count = 0
    while count < 4:
        for i, item in enumerate(sorted_x):
            for j, char in enumerate(item[1]):
                if count > 4:
                    return True
                if checksum[count] not in item[1]:
                    return False
                count += 1
    return True
    

print(real_rooms(PUZZLE))
print(f"Solution to part 1 is: {PART_1}")