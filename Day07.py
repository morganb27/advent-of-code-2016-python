import re

PUZZLE = [line.strip() for line in open("input.txt")]
PART_1 = 0
PART_2 = 0

def parse_address(address):
    runs = re.findall(r"(\w+)", address)
    return runs[1::2], runs[::2]

def is_abba(address):
    for i in range(len(address) - 3):
        a, b, c, d = address[i:i+4]
        if a == d and b == c and a != b:
            return True
    return False

def find_abas(address):
    for i in range(len(address) - 2):
        a, b, c = address[i:i+3]
        if a == c and a != b:
            yield a, b 

for line in PUZZLE:
    inside, outside = parse_address(line)
    
    # Part 1
    if not any(is_abba(sequence) for sequence in inside) and any(is_abba(sequence) for sequence in outside):
        PART_1 += 1
    
    # Part 2
    for seq_outside in outside:
        found = False
        abas = find_abas(seq_outside)

        for a, b in abas:
            bab = b + a + b

            if any(b+a+b in seq_inside for seq_inside in inside) and not found:
                PART_2 += 1
                found = True




print("PART_1:", PART_1)
print("PART_2", PART_2)





