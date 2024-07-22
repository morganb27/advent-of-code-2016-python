import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
CODE_1 = ''
CODE_2 = ''

KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

KEYPAD_2 = [
    ['_' , '_' , 1 ,'_', '_'],
    ['_' ,  2  , 3 , 4 , '_'],
    [ 5  ,  6  , 7,  8 ,  9 ],
    ['_', 'A', 'B', 'C', '_'],
    ['_', '_', 'D', '_', '_'],
]

DIRS = {
    'U' : (-1, 0),  
    'R' : (0, 1),  
    'D' : (1, 0), 
    'L' : (0, -1) 
}

def bathroom_security(data):
    global CODE_1, CODE_2
    pos_1 = [1, 1]
    pos_2 = [2, 0]
    for line in data:
        for x in line:
            pos_1 = move(KEYPAD, pos_1, x)
            pos_2 = move(KEYPAD_2, pos_2, x)
        CODE_1 += str(KEYPAD[pos_1[0]][pos_1[1]])
        CODE_2 += str(KEYPAD_2[pos_2[0]][pos_2[1]])


def move(keypad, pos, d):
    x, y = pos[0] + DIRS[d][0], pos[1] + DIRS[d][1]
    new = [x, y]

    if new[0] < 0 or new[0] >= len(keypad):
        return pos
    
    if new[1] < 0 or new[1] >= len(keypad[0]):
        return pos
    
    if keypad[x][y] == '_':
        return pos
    
    return new


bathroom_security(PUZZLE)
print(f"Solution for part 1 is: {CODE_1}")
print(f"Solution for part 2 is: {CODE_2}")
