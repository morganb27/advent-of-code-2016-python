PUZZLE = [list(map(int, line.strip().split())) for line in open("input.txt")]
PART_1, PART_2 = 0, 0

for line in PUZZLE:
    a, b, c = sorted(line)
    if a + b > c:
        PART_1 += 1

for col in range(3):
    for row in range(0, len(PUZZLE) - 2, 3):
        a, b, c = sorted([PUZZLE[row][col], PUZZLE[row + 1][col], PUZZLE[row + 2][col]])

        if a + b > c:
            PART_2 += 1
        

print("PART 1:", PART_1)
print("PART 2:", PART_2)
