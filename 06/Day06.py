import fileinput
from collections import Counter

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = '', ''


def signal_and_noise(data):
    global PART_1, PART_2
    for j in range(len(data[0])):
        col = ''
        for i in range(len(data)):
            col += data[i][j]
        count = Counter(col)
        PART_1 += count.most_common()[0][0]
        PART_2 += count.most_common()[-1][0]
            
        



signal_and_noise(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")