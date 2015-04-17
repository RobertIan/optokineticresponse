#!/usr/bin/env python

from psychopy import visual, core, event
import time
import csv
import os

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

#create timers
clock = core.Clock()
interval1start = 30
interval1stop = 60
interval2start = 90
interval2stop = 120
interval3start = 150
interval3stop = 180
triallength = 210

#create a window
fullscreen = (1920, 1080)
win2 = visual.Window(screen=0, size=fullscreen, pos=(0, 0))

#create the stimuli
opto1 = visual.GratingStim(win=win2, size=fullscreen, tex='sqr',  pos=[0,0], sf=250000, color= [1,1,1])
opto2 = visual.GratingStim(win=win2, size=fullscreen, tex='sqr', pos=[0,0], sf=25000, color= [1,1,1])
opto3 = visual.GratingStim(win=win2, size=fullscreen, tex='sqr', pos=[0,0], sf=2500, color= [1,1,1])

#draw the stimuli and update the window
while 1:
    print clock.getTime()
    if interval1start<clock.getTime()<interval1stop : #this creates a never-ending loop
        opto1.setPhase(0.05, '+')#advance phase by 0.05 of a cycle
        opto1.color -= [0.001, 0.001, 0.001]
        opto1.draw()
        win2.flip()
    if interval1stop<clock.getTime()<interval2start : #this creates a never-ending loop
        win2.flip()
    if interval2start<clock.getTime()<interval2stop : #this creates a never-ending loop
        opto2.setPhase(0.05, '+')#advance phase by 0.05 of a cycle
        opto2.color -= [0.001, 0.001, 0.001]
        opto2.draw()
        win2.flip()
    if interval2stop<clock.getTime()<interval3start : #this creates a never-ending loop
        win2.flip()
    if interval3start<clock.getTime()<interval3stop : #this creates a never-ending loop
        opto3.setPhase(0.05, '+')#advance phase by 0.05 of a cycle
        opto3.color -= [0.001, 0.001, 0.001]
        opto3.draw()
        win2.flip()
    if interval3stop<clock.getTime()<triallength:
        win2.flip()
    if len(event.getKeys())>0:
        event.clearEvents()
        break
    if triallength<clock.getTime():
        break

#cleanup
win2.close()
core.quit()


