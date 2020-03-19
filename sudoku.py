import time




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

def print_board():
    global Table
    print()
    for i in range (9):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - -")

        for j in range(9):
            if j%3 == 0 and j !=0:
                print("|", end="")
            print(str(Table[i][j]) + " ", end="")
            if j == 8:
                print()
    print()


def solve():
    time.sleep(0.0005)
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
