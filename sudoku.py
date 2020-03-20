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
         [0,0,0,0,0,0,0,0,0]]

colours_default = []
Colours = []

for i in range(81):
    if i < 27:
        if i // 3 == 1 or i // 3 == 4 or i // 3 == 7:
            colours_default.append((181, 186, 182))
        else:
            colours_default.append((255,255,255))
    elif i > 26 and i < 54:
        if i // 3 == 10 or i // 3 == 13 or i // 3 == 16:
            colours_default.append((255, 255, 255))
        else:
            colours_default.append((181, 186, 182))
    else:
        if i // 3 == 19 or i // 3 == 22 or i // 3 == 25:
            colours_default.append((181, 186, 182))
        else:
            colours_default.append((255, 255, 255))
    Colours.append(colours_default[i])



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
    if solve():
        pass
    global Done_Solving
    Done_Solving = True

def solve():
    time.sleep(0.005)
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
            if solve():
                return True
            else:
                Table[y][x] = 0
    return False
