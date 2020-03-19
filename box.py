import pygame

pygame.init()
font = pygame.font.Font('Font.ttf', 24)
font_small = pygame.font.Font('Font.ttf', 15)
class Box:
    def __init__(self, surface, colour, size, width, number = 0, fill = (255,255,255)):
        self.s = surface
        self.sz = size
        self.w = width
        self.c = colour
        self.n = str(number)
        self.f = fill

    def fill(self, colour=(255, 255, 255)):
        self.f = colour


    def draw(self):
        self.s.fill(self.f, self.sz)
        pygame.draw.rect(self.s,self.c,self.sz,self.w)

    def change_color(self, colour):
        self.c = colour

    def get_size(self):
        return self.sz

    def display_num(self):
        num = font.render(str(self.n), True, (0,0,0))
        (x,y,w,h) = self.sz
        self.s.blit(num, (x+w/2.8,y+h/4))

    def change_num(self,number):
        self.n = number

    def display_string(self, text):
        num = font_small.render(text, True, (0,0,0))
        (x, y, w, h) = self.sz
        self.s.blit(num, (x+ w /10, y + h/ 10))