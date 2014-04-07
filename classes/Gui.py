import pygame
from pygame import *
from Fields import *

class Gui(object):

    def __init__(self):
        self.size = self.weight, self.height = 800, 640
        self.window = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

        #instantinating field
        self.init_grid()
        self.draw_grid()

    #initiate fields
    def init_grid(self):
        self.f = [[], [], []]
        for x in range(0, 3):
            for y in range(0, 3):
                self.f[x].append(Fields(x, y))

    #called at initialisation
    def draw_grid(self):
        for x in range(0, 3):
            for y in range(0, 3):
                self.f[x][y].draw(self.window)

    def render_grid(self):
        for x in range(0,3):
            for y in range(0,3):
                self.f[x][y].render(self.window)

    def get_rect_adress(self, mx, my):
        for a in range(3):
            print "a:", a
            for b in range(3):
                print "b:", b
                for c in range(3):
                    print "c:", c
                    for d in range(3):
                        print "d:", d
                        left = self.f[a][b].b[c][d].left
                        right = self.f[a][b].b[c][d].left + Boxes.width
                        top = self.f[a][b].b[c][d].top
                        bottom = self.f[a][b].b[c][d].top + Boxes.height
                        if (left < mx and mx < right and top < my and my < bottom):
                            return b, a, d, c

    def is_grid_won(self):
        for a in range(3):
            for b in range(3):
                if self.f[a][b].is_field_won():
                    return self.f[a][b].is_field_won()
