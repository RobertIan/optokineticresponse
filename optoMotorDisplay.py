#!/usr/bin/env python

import pygame
import sys
import os
import time
from pygame.locals import *
import cv2

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

#csv file open
f = d+'.csv'
try:
    fsize = os.stat(f).st_size 
except FileNotFoundError:
    w = csv.writer(open(f, 'w'), delimiter=',')
    w.writerow(['date','trial time start','collection time','scroll speed','scroll direction'])
else:
    if fsize > 0:
        w = csv.writer(open(f, 'a'), delimiter=',')

# video recorder
fourcc = cv2.cv.CV_FOURCC(*'MPEG')  
video_writer = cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))

# record video
x = screenWidth
while (capture.isOpened()):
    if pygame.time.get_ticks() > 60000:
#        w.write('Trial has ended.\n')
#        w.write('     Time elapsed: '+str(pygame.time.get_ticks()/1000)+' seconds.\n')
#        w.write('     Speed: '+str(speed)+' pixels/ms.\n')
#        w.write('     Date: '+time.strftime('%c')+'\n')
#        w.close()
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                break
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
                                  #if increased to 10, it w
    
    
capture.release()
video_writer.release()
cv2.destroyAllWindows()


######################################
'''
x += 1  # spinning --> clock
if x == screenWidth:  # spinning --> clock
    x = 0  # spinning --> clock
'''



