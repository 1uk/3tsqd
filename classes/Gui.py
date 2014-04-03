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

    def init_grid(self):
        self.f = [[], [], []]
        for y in range(0, 3):
            for x in range(0, 3):
                self.f[x].append(Fields(x, y))

    #at initialisation
    def draw_grid(self):
        for y in range(0, 3):
            for x in range(0, 3):
                self.f[x][y].draw(self.window)

    def render_grid(self):
        for x in range(0,3):
            for y in range(0,3):
                self.f[x][y].render(self.window)

    def get_rect_adress(self, mx, my):
            for a in range(0,3):
                if (self.f.[a][b].left < mx):
                    if (self.f[a][b].left.  < my):
                            
                    
                    for c in range(0,3):
                        for d in range(0,3):
                            left = self.f[a][b].b[c][d].left
                            top = self.f[a][b].b[c][d].top
                            right = left + self.f[a][b].b[c][d].width
                            down = top + self.f[a][b].b[c][d].height

            if (left <= mx and mx <= left + width):
                x = a
                xx = c
            if (top <= my and my <= top + height):
                y = b
                yy = d


