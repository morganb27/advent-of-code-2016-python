import re
from collections import Counter
from utils import ALPHABET

PUZZLE = [line.strip() for line in open("input.txt")]
PART_1 = 0

for line in PUZZLE:
    deciphered = ""
    name, id, checksum = re.search(r"([\w-]+)-(\d+)\[(\w+)\]", line).groups()
    counts = Counter(char for char in name if char != '-')
    expected = "".join(char for char, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:5])
    
    #Part 1
    if expected == checksum:
        PART_1 += int(id)

    #Part 2
    rotate = int(id) % 26
    deciphered = "".join(
        " " if char == "-" else ALPHABET[(ALPHABET.index(char) + rotate) % len(ALPHABET)] for char in name
    )

    if "northpole" in deciphered:
        PART_2 = id


print("PART_1:", PART_1)
print("Part_2:", PART_2)