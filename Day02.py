
PUZZLE = [line.strip() for line in open("input.txt")]
PART_1, PART_2 = '', ''
DIRS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
row, col = 1, 1
row_two, col_two = 2, 0

KEYPAD_TWO = {
    (0, 2): '1',
    (1, 1): '2', (1, 2): '3', (1, 3): '4',
    (2, 0): '5', (2, 1): '6', (2, 2): '7', (2, 3): '8', (2, 4): '9',
    (3, 1): 'A', (3, 2): 'B', (3, 3): 'C',
    (4, 2): 'D'

}


for line in PUZZLE:
    for dir in line:
        dr, dc = DIRS[dir]
        row = max(0, min(2, row + dr))
        col = max(0, min(2, col + dc))
    PART_1 += str(row*3 + col + 1)


for line in PUZZLE:
    for dir in line:
        dr, dc = DIRS[dir]
        new_row, new_col = row_two + dr, col_two + dc
        if (new_row, new_col) in KEYPAD_TWO:
            row_two, col_two = new_row, new_col
    PART_2 += KEYPAD_TWO[(row_two, col_two)]


print('PART 1:', PART_1)
print('PART 2:', PART_2)