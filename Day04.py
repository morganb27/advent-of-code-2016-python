import re
from collections import Counter

PUZZLE = [line.strip() for line in open("input.txt")]
PART_1 = 0

for line in PUZZLE:
    name, id, checksum = re.search(r"([\w-]+)-(\d+)\[(\w+)\]", line).groups()
    counts = Counter(char for char in name if char != '-')
    expected = "".join(char for char, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:5])
    
    if expected == checksum:
        PART_1 += int(id)

print("PART_1:", PART_1)