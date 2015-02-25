#!/usr/bin/env python

import pygame
import sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

######################################
b1 = 'opto1.png'               #
#b1 = '*.png'                  # we need to start to measure and define these by contrast and acuity angle
######################################

back = pygame.image.load(b1).convert()
back2 = pygame.image.load(b1).convert()


screenWidth = 800

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

