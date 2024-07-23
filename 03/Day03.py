import fileinput

PUZZLE = [[int(x) for x in line.split()] for line in fileinput.input()]
PART_1 = 0
PART_2 = 0

def valid_triangles(data):
    global PART_1
    for line in data:
        a, b, c = line
        if is_valid_triangle(a, b, c):
            PART_1 += 1
    return

def valid_triangles_part_two(data):
    global PART_2
    for j in range(len(data[0])):
        for i in range(0, len(data) - 2, 3):
            a, b, c = data[i][j], data[i+1][j], data[i+2][j]
            if is_valid_triangle(a, b, c):
                PART_2 += 1
    return

def is_valid_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    return True
    


valid_triangles(PUZZLE)
valid_triangles_part_two(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")
