import fileinput

PUZZLE = (line.strip().split(', ') for line in fileinput.input())

DIRS = [
    (0, 1),  #North
    (1, 0),  #East
    (0, -1), #South
    (-1, 0)  #West
]

def easter_bunny_HQ(data):
    position = [0, 0] 
    facing = 0
    seen = set()
    for line in data:
        for dir in line:
            turn, steps = dir[0], int(dir[1:])
            if turn == 'L':
                facing = (facing - 1) % 4
            else:
                facing = (facing + 1) % 4
            for _ in range(steps):
                position[0] += DIRS[facing][0] 
                position[1] += DIRS[facing][1]

                if (position[0], position[1]) in seen:
                    print(f"Poisiton already visited: {position[0], position[1]}. Solution to part 2 is: {abs(position[0]) + abs(position[1])}")
                    return
                seen.add((position[0], position[1]))
    return abs(position[0]) + abs(position[1])

print(f"Solution to part 1 is: {easter_bunny_HQ(PUZZLE)}")