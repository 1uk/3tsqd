import pygame
from pygame.locals import *

import Fields

class Boxes(object):

    #static variables
    width = 60
    height = 60
    gap = 10

    def __init__(self, x, y, parent_x, parent_y):
        #Status Leer 0, Kreuz 1, Kreis 2
        self.state = 0
        self.left = parent_x + x * (self.width + self.gap)
        self.top = parent_y + y * (self.height + self.gap) 
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

        #debug
        self.a=0

    def draw(self, window, color):
        pygame.draw.rect(window, color, self.rect)

    def fill(self, window):
        #cross
        if (self.state == 1):
            if self.a < 1:
                print "draw: self.top:", self.top, "self.left:", self.left
            margin = 10
            left = self.left + margin
            right = self.left + self.width - margin
            top = self.top + margin
            bottom = self.top + self.height - margin
            if self.a < 1:
                print "draw: top:",top,"left:",left
                self.a += 1
            #line from pn to en
            p1 = (left, top)
            e1 = (right, bottom)
            p2 = (left, bottom)
            e2 = (right, top)
            pygame.draw.line(window, 0x000000, p1, e1, 8)
            pygame.draw.line(window, 0x000000, p2, e2, 8)
        #circle
        elif (self.state == 2):
            if self.a < 1:
                print "draw: top:", self.top, "left:", self.left
            x = self.left + self.width/2
            y = self.top + self.height/2
            if self.a < 1:
                print "Mitte: x:", x, "y:", y
                self.a += 1
            pygame.draw.circle(window, 0x000000, (x, y), 20, 8)
