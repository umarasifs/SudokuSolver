import pygame
import box
import sudoku
import threading
import sys



#initialization
pygame.init()
height, width = 700,500
font = pygame.font.Font('Font.ttf', 24)
font_small = pygame.font.Font('Font.ttf', 15)


#screen size
screen = pygame.display.set_mode((width, height))
screen.fill((247,247,223))

#Title and Icon
pygame.display.set_caption("Sudoku + Solver")
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

#Border
Border = box.Box(screen,(0,0,0),(width/ 20, height /7, width *18 /20, width*18/20),
                 width//100)

#3x3 Boxes
Big_Boxes = []
for i in range(3):
    for j in range(3):
        Big_Boxes.append(box.Box(screen, (0,0,0),
                                 (width/20 + width*3*j/10, height/7 + width*3*i/10,width*3/10, width*3/10),
                                 3))

#1x1 Boxes
Small_Boxes = []
for i in range(9):
    for j in range(9):
        Small_Boxes.append(box.Box(screen, (0,0,0),
                                   (width/20 + width*j/10, height/7 + width*i/10, width/10, width/10), 1))

#reset button
reset = box.Box(screen, (0,0,0), (width *17 //20, height // 20, width //10, height// 20),1)

#state values
box_pressed = False
box_pressed_num = None
solving = False

#display text
def display_text(fonts, text, pos, color = (0,0,0)):
    string = fonts.render(text, True, color)
    screen.blit(string, pos)


#update boxes on the screen
def update():
    reset.draw()
    reset.display_string("Reset")
    Border.draw()
    for i in range(9):
        Big_Boxes[i].draw()
        for j in range(9):
            Small_Boxes[9 * i + j].change_num(sudoku.Table[i][j])
    for i in range(81):
        Small_Boxes[i].fill(sudoku.Colours[i])
        Small_Boxes[i].draw()
        Small_Boxes[i].display_num()
    pygame.display.update()

def update_lite():
    for i in range(9):
        for j in range(9):
            z = 9 * i + j
            Small_Boxes[z].change_num(sudoku.Table[i][j])
            Small_Boxes[z].fill(sudoku.Colours[z])
            Small_Boxes[z].draw()
            Small_Boxes[z].display_num()
    pygame.display.update( (width// 20, height //7, width *9 //10, width*9//10))




#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            solving = False
            running = False
            pygame.quit()
            sys.exit()
        if not solving :
            (x,y)= pygame.mouse.get_pos()
            (x0,y0, w,h) = reset.get_size()
            if x >= x0 and x <= x0 + w and y >= y0 and y <= y0 + h:
                reset.fill((163, 162, 157))
            else:
                reset.fill((191, 190, 184))
            if box_pressed:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        box_pressed = False
                        Small_Boxes[box_pressed_num].change_color((0,0,0))
                        if sudoku.Table[box_pressed_num // 9][box_pressed_num % 9] != 0:
                            sudoku.Colours[box_pressed_num] = (119, 235, 77)
                        else:
                            sudoku.Colours[box_pressed_num] = sudoku.colours_default[box_pressed_num]


                    if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 0
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 1
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 2
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 3
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 4
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 5
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 6
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 7
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 8
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        sudoku.Table[box_pressed_num // 9][box_pressed_num %9] = 9



            if not box_pressed:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_CAPSLOCK:
                        sudoku.Table =  [[8,0,0,0,0,0,0,0,0],
                                         [0,0,3,6,0,0,0,0,0],
                                         [0,7,0,0,9,0,2,0,0],
                                         [0,5,0,0,0,7,0,0,0],
                                         [0,0,0,0,4,5,7,0,0],
                                         [0,0,0,1,0,0,0,3,0],
                                         [0,0,1,0,0,0,0,6,8],
                                         [0,0,8,5,0,0,0,1,0],
                                         [0,9,0,0,0,0,4,0,0]]
                        for y in range(9):
                            for x in range(9):
                                if sudoku.Table[y][x] != 0:
                                    sudoku.Colours[y * 9 + x]=(119, 235, 77)

                    if event.key == pygame.K_SPACE:
                        solving = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y)= pygame.mouse.get_pos()
                    (x0, y0, w, h) = reset.get_size()
                    if x >= x0 and x <= x0+w and y >= y0 and y <=y0+h:
                        for i in range(9):
                            for j in range(9):
                                sudoku.Table[i][j] = 0
                        for i in range(81):
                            sudoku.Colours[i] = sudoku.colours_default[i]
                    (x0,y0, w,h) = Border.get_size()
                    if x >= x0 and x <= x0+w and y >= y0 and y <=y0+h:
                        for i in range(9):
                            (x0,y0, w, h) = Big_Boxes[i].get_size()
                            if x >= x0 and x <= x0+w and y >= y0 and y <=y0+h:
                                for j in range(9):
                                    (x0,y0, w,h) = Small_Boxes[i//3 * 27 + i%3*3 + j%3 + j//3*9].get_size()
                                    if x >= x0 and x <= x0+w and y >= y0 and y <=y0+h:
                                        box_pressed_num = i//3 * 27 + i%3*3 + j%3 + j//3*9
                                        box_pressed = True
                                        sudoku.Colours[i//3 * 27 + i%3*3 + j%3 + j//3*9]=(237,203,164)
                                        Small_Boxes[i//3 * 27 + i%3*3 + j%3 + j//3*9].change_color((0,0,255))
                                        break
                            if box_pressed == True:
                                break



    display_text(font, "SUDOKU SOLVER", (width /3.1, height /20))
    display_text(font_small, "Click on a box to change a box' value using the keypad.", (width/100, height *17 /20))
    display_text(font_small, "Press ENTER when done. Press SPACE to Solve", (width / 100, height * 18 / 20))

    update()

    t = threading.Thread(target=sudoku.complete)
    if solving:
        t.start()
    while not sudoku.Done_Solving and solving:
        pygame.event.get()
        l = threading.Thread(target=update_lite)
        l.start()
        l.join()
    if solving:
        t.join()
        sudoku.Done_Solving=False
    solving =False



