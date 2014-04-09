import pygame
from pygame import *
from Fields import *

class Gui(object):

    def __init__(self):
        self.size = self.weight, self.height = 640, 640
        self.window = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

        #instantinating field
        self.init_grid()
        self.draw_grid()

    #initiate fields
    def init_grid(self):
        self.f = [[], [], []]
        for x in range(3):
            for y in range(3):
                self.f[x].append(Fields(x, y))
                print "init: x:", x, "y:", y

    #called at initialisation
    def draw_grid(self):
        for x in range(3):
            for y in range(3):
                self.f[x][y].draw(self.window)

    def render(self):
        for x in range(3):
            for y in range(3):
                self.f[x][y].render(self.window)

    def get_rect_adress(self, mx, my):
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    for d in range(3):
                        left = self.f[a][b].b[c][d].left
                        right = self.f[a][b].b[c][d].left + Boxes.width
                        top = self.f[a][b].b[c][d].top
                        bottom = self.f[a][b].b[c][d].top + Boxes.height
                        if (left < mx and mx < right and top < my and my < bottom):
                            return a, b, c, d

    def is_won(self, x, y):
        #x axis
        b = 1
        while self.f[x][y].state == self.f[x][(y+b)%3].state:
            if b == 2:
                return self.f[x][y].state
            b += 1
        #y achsis
        b = 1
        while self.f[x][y].state == self.f[(x+b)%3][y].state:
            print self.f[x][y].state == self.f[(x+b)%3][y].state
            if b == 2:
                return self.f[x][y].state
            b += 1
        #diagonal up
        a, b = 0, 0
        while self.f[a][b].state == self.f[a+1][b+1].state:
            if b == 1:
                return self.f[a][b].state
            a += 1
            b += 1
        #diagonal down
        a, b = 0, 2
        while self.f[a][b].state == self.f[a+1][b-1].state:
            if b == 1:
                return self.f[a][b].state
            a += 1
            b -= 1
        #nobody has won
        return 0

    def won(self, player):
        myfont = pygame.font.SysFont("monospace", 40)
        mylittlefont = pygame.font.SysFont("monospace", 15)

        #render text
        label1 = myfont.render("WINNER: Player" + str(player), 1, (255,255,255))
        label2 = myfont.render("TO EXIT PRESS [ESC]", 1, (255,255,255))
        self.window.blit(label1, (10, 320))
        self.window.blit(label2, (100, 500))
