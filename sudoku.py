import time


Done_Solving = False

Table = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]

Colours = []
for i in range(81):
    Colours.append((255,255,255))


def find_empty():
    global Table
    for y in range(9):
        for x in range(9):
            if Table[y][x] == 0:
                return (y,x)
    return None

def check(y,x,z):
    global Table
    f = x // 3 * 3
    g = y // 3 * 3
    for a in range(9):
        if Table[a][x] == z:
            return False
    for a in range(9):
        if Table[y][a] == z:
            return False
    for a in range(3):
        for b in range(3):
            if Table[b+g][a+f] == z:
                return False
    return True

def complete():
    if solve(0.005):
        global Done_Solving
        Done_Solving = True

def quick_solve():
    if solve(0):
        global Done_Solving
        Done_Solving = True

def solution_check():
    return solve(0)

def solve(sec):
    time.sleep(sec)
    global Table
    pos = find_empty()
    if not pos:
        return True
    else:
        y, x = pos

    for z in range(1,10):
        Colours[y * 9 + x]=((235, 83, 77))
        if check(y,x,z):
            Table[y][x] = z
            Colours[y * 9 + x]=((119, 235, 77))
            if solve(sec):
                return True
            else:
                Table[y][x] = 0
    return False
