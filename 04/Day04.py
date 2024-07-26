import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1 = 0
PART_2 = 0

def real_rooms(data):
    global PART_1
    for line in data:
        name, id, checksum = parse_input(line)
        if is_real_room(name, checksum):
            PART_1 += int(id)

def north_pole(data):
    global PART_2
    for line in data:
        name, rotate, checksum = parse_input(line)
        if decrypt(name, rotate) == 'northpole object storage':
            PART_2 = rotate
            return f'North pole objects found at id: {rotate}'
    return -1
        

def decrypt(name, rotate):
    res = ''
    for char in name:
        if char.isalpha():
            steps = int(rotate) % 26
            for _ in range(steps): 
                char = move(char)
            res += char
        else:
            res += ' '
    return res

def move(char):
    if char == 'z':
        return 'a'
    return chr(ord(char) + 1)




def parse_input(line):
    name, right = line.rsplit('-', 1)
    id, checksum = right.strip(']').split('[')
    return name, id, checksum

def is_real_room(name, checksum):
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
    

real_rooms(PUZZLE)
north_pole(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")