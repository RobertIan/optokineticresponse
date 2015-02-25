#!/usr/bin/env python

import pygame
import sys
from pygame.locals import *
import pygame.camera
pygame.init()
pygame.canera.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.caemra.Camera(camlist[0],(640,480))

######################################
b1 = 'opto1.png'               #
#b1 = '*.png'                  # we need to start to measure and define these by contrast and acuity angle
######################################

back = pygame.image.load(b1).convert()
back2 = pygame.image.load(b1).convert()


screenWidth = 800 #  not used in fullscreen

#######################################
#'''
x = screenWidth  # spinning <-- counter
speed0 = 1
speed = speed0
#'''
'''
x = 0  # spinning --> clock
'''
#######################################

class Capture(object):
    def __init__(self):
        self.size = (640,480)
        # create a display surface. standard pygame stuff
        self.display = pygame.display.set_mode(self.size, 0)
        
        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # if you don't want to tie the framerate to the camera, you can check 
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # blit it to the display surface.  simple!
        self.display.blit(self.snapshot, (0,0))
        pygame.display.flip()

    def main(self):
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False

            self.get_and_flip()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                pygame.time.wait(5000)
            if event.key == pygame.K_r:
                x *= -1
                screenWidth *= -1 #press r to reverse direction
            if event.key == pygame.K_4:
                speed -= 1        #press 4 to decrease speed in increment of 1
                                  #if decreased to 0, it will revert to normal speed
            if event.key == pygame.K_5:
                speed += 1        #press 5 to increase speed in increment of 1
                                  #if increased to 10, it will revert to normal speed
    
    ######################################
    '''
    x += 1  # spinning --> clock
    if x == screenWidth:  # spinning --> clock
        x = 0  # spinning --> clock
    '''

    #'''
    if x > 0:
        x -= speed 
    elif x == 0:  # spinning <-- counter
        x = screenWidth  # spinning <-- counter
    else:
        x += speed
    if speed == 0:
        speed = speed0
    if speed == 10:
        speed = speed0
    #'''
    
    screen.blit(back, (x, 0))
    screen.blit(back2, (x-screenWidth, 0))
    ######################################

    ######################################
    msElapsed = clock.tick(300)
    ######################################
    pygame.display.flip()

