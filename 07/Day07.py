import fileinput
import re

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, 0

def onCreated():
    support_tls()
    is_aba()

def support_tls(data):
    global PART_1, PART_2
    for line in data:
        parts = re.findall('(\\w+)', line)
        if is_abba(parts[::2]) and not is_abba(parts[1::2]):
            PART_1 += 1
        sequences = search_aba(parts[::2])
        hypernet = search_aba(parts[1::2])
        if is_aba(sequences, hypernet):
            PART_2 += 1
        

def is_abba(parts):
    for part in parts:
        for i in range(len(part) - 3):
            if part[i] == part[i+3] and part[i+1] == part[i+2] and part[i] != part[i+1]:
                return True
    return False

def is_aba(sequences, hypernet):
    for sequence in sequences:
            a, b, c = list(sequence)
            for h in hypernet:
                if b + a + b == h:
                    return True
    return False

def search_aba(parts):
    aba = []
    for part in parts:
        for i in range(len(part) - 2):
            if part[i] == part[i+2] and part[i] != part[i+1] and len(part[i:i+3]) == 3:
                aba.append(part[i:i+3])
    return aba


support_tls(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")


