from collections import Counter

PUZZLE = [line.strip() for line in open("input.txt")]
PART_1, PART_2 = "", ""

for col in range(len(PUZZLE[0])):
    c = Counter()
    for row in range(len(PUZZLE)):
        char = PUZZLE[row][col]
        c[char] += 1
    PART_1 += c.most_common(1)[0][0]
    PART_2 += c.most_common()[-1][0]

print("PART_1", PART_1)
print("PART_2", PART_2)

