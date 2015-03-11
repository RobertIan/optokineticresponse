#!/usr/bin/env python

import pygame
import sys
import os
import time
import cv2
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

screenWidth = 800
screen = pygame.display.set_mode((screenWidth, 600), pygame.FULLSCREEN)

b1 = 'opto1.png' 

back = pygame.image.load(b1).convert()
back2 = pygame.image.load(b1).convert() #repeats itself

capture = cv2.VideoCapture(0)

#date and time variable creation
d = time.strftime('%m%d%Y')
now = time.strftime('%X')

#open output csv file for writing or appending
f = d+'.csv'
try:
    fsize = os.stat(f).st_size 
except OSError:
    w = csv.writer(open(f, 'w'), delimiter=',')
    w.writerow(['date','trial time start','collection time','scroll speed','scroll direction'])
else:
    if fsize > 0:
        w = csv.writer(open(f, 'a'), delimiter=',')

#set timer to pause screen every 30 seconds
pygame.time.set_timer(USEREVENT+1, 60000)

# video recorder
fourcc = cv2.cv.CV_FOURCC(*'MPEG')  
video_writer = cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))

# record video
x = screenWidth
while (capture.isOpened()):
    if pygame.time.get_ticks() > 600000:
        w.writerow([d,now,pygame.time.get_ticks(),speed,dir])
        break
    speed0 = 50
    speed = speed0
    if x > 0:
        x -= speed 
    elif x == 0:  # spinning <-- counter
        x = screenWidth  # spinning <-- counter
    else:
        x += speed
    if speed == 0:
        speed = speed0
    if speed == 100:
        speed = speed0
    

    screen.blit(back, (x, 0))
    screen.blit(back2, (x-screenWidth, 0))
    ######################################

    ######################################
    
    ######################################

    pygame.display.flip()
    ret, frame = capture.read()
    if ret:
        video_writer.write(frame)
    else:
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == USEREVENT+1:
            pygame.time.wait(30000)
            w.writerow([d,start,pygame.time.get_ticks(),speed,dir])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                break
            if event.key == pygame.K_SPACE:
                pygame.time.wait(30000)     #press spacebar to pause program for 30 seconds
            if event.key == pygame.K_r:
                x *= -1
                screenWidth *= -1           #press r to reverse direction
            if event.key == pygame.K_4:
                speed -= 1                  #press 4 to decrease speed in increment of 1
                                            
            if event.key == pygame.K_5:
                speed += 1                  #press 5 to increase speed in increment of 1
                                           
    
    
capture.release()
video_writer.release()
cv2.destroyAllWindows()


######################################
'''
x += 1  # spinning --> clock
if x == screenWidth:  # spinning --> clock
    x = 0  # spinning --> clock
'''



