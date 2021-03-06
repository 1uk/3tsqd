import pygame
from pygame.locals import *
from Boxes import *

import time

class Fields(object):

    #static variables
    width = 200
    height = 200
    gap = 20

    def __init__(self, x, y):
        #Status hot 0, player 1, player 2, full 3
        self.state = 0
        self.bide = True

        self.left = x * (self.width + self.gap)
        self.top = y * (self.height + self.gap)
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        #instantinating boxes
        self.init_boxes()

    def init_boxes(self):
        self.b = [[], [], []]
        for x in range(3):
            for y in range(3):
                self.b[x].append(Boxes(x, y, self.left, self.top))



    def render(self, window):
        #redraw the boxes
        self.draw(window) #redraws the wrong field?!
        #refill the boxes
        self.fill(window)

    def draw(self, window):
        #highlighting
        color = BLUE = (40, 40, 255)
        DBLUE = (100, 100, 255)
        if self.bide:
            color = DBLUE

        #draw box
        for x in range(0,3):
            for y in range(0,3):
                self.b[x][y].draw(window, color)

    def fill(self, window):

        #fill boxes
        for x in range(0,3):
            for y in range(0,3):
                self.b[x][y].fill(window)

        #fill field, if field is won
        if self.state:
            #diameter
            dm = 20
            BLACK = (0, 0, 0)
            margin = 20
            #player 1 has won the field
            if (self.state == 1):
                left = self.left + margin
                right = self.left + self.width - margin
                top = self.top + margin
                bottom = self.top + self.height - margin
                #line from pn to en
                p1 = (left, top)
                e1 = (right, bottom)
                p2 = (left, bottom)
                e2 = (right, top)
                pygame.draw.line(window, BLACK, p1, e1, dm)
                pygame.draw.line(window, BLACK, p2, e2, dm)
            #player 2
            elif (self.state == 2):
                x = self.left + self.width/2
                y = self.top + self.height/2
                pygame.draw.circle(window, BLACK, (x, y), (self.width - margin)/2, dm)




    def is_won(self, x, y):
        #x axis
        b = 1
        while self.b[x][y].state == self.b[x][(y+b)%3].state:
            if b == 2:
                return self.b[x][y].state
            b += 1
        #y achsis
        b = 1
        while self.b[x][y].state == self.b[(x+b)%3][y].state:
            print "self.b[",x,"][",y,"] == self.b[",(x+b)%3,"][",y,"]"
            print self.b[x][y].state == self.b[(x+b)%3][y].state
            if b == 2:
                return self.b[x][y].state
            b += 1
        #diagonal up
        a, b = 0, 0
        while self.b[a][b].state == self.b[a+1][b+1].state:
            if b == 1:
                return self.b[a][b].state
            a += 1
            b += 1
        #diagonal down
        a, b = 0, 2
        while self.b[a][b].state == self.b[a+1][b-1].state:
            if b == 1:
                return self.b[a][b].state
            a += 1
            b -= 1
        #nobody has won
        return 0
