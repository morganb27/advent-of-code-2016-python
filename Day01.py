from utils import Point

PUZZLE = [(s[0], int(s[1:])) for s in open("input.txt").read().strip().split(", ")]
FACING, POS = 0, Point(0, 0)
SEEN = {Point(0, 0)}
PART_2 = None
DIRS_4 = {
    0: Point(0, 1),  # N 
    1: Point(1, 0),  # E 
    2: Point(0, -1), # S 
    3: Point(-1, 0), # W 
}


for dir, steps in PUZZLE:
    FACING = (FACING + 1) % 4 if dir == 'R' else (FACING - 1) % 4
    for _ in range(steps):
        POS += DIRS_4[FACING]

        if PART_2 is None and POS in SEEN:
            PART_2 = abs(POS.x) + abs(POS.y)
        else:
            SEEN.add(POS)


PART_1 = abs(POS.x) + abs(POS.y)
print("PART_1", PART_1)
print("PART_2", PART_2)
