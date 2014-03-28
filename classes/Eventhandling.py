import pygame
from pygame import event

class Eventhandling(object):
    #handles events
    def __init__(self):
        pass

    def on_event(self, event):
        print "EVENT!"
        if event.type == MOUSEBUTTONDOWN:
            print "MAUSKLICK!"
            if event.button == 1:
                print "LINKS"
                on_lbutton_down(event)

    def on_lbutton_down(self, event):
        #get mouse coordinates
        mx, my = pygame.mouse.get_pos()
        print "Mausposition:", event.pos
        print "Field: [", mx/200, "]", "[", my/200, "]"
        print "mx:", mx, "my:", my

        #check in which rect mouse is in
        #for a in range(0,3):
        #     for b in range(0,3):
        #        for c in range(0,3):
        #            for d in range(0,3):
        #                left = self.f[a][b].b[c][d].left
        #                top = self.f[a][b].b[c][d].top
        #                width = self.f[a][b].b[c][d].width
        #                height = self.f[a][b].b[c][d].height
#
#                        if (left <= mx and mx <= left + width):
#                            x = a
#                            xx = c
#                        if (top <= my and my <= top + height):
#                            y = b
#                            yy = d
#        self.f[x][y].b[xx][yy].fill(0, self.window)
        #print "Geklickt:", x, "-", y, "-", xx, "-" ,yy


    def on_escape_down(event):
        return False
