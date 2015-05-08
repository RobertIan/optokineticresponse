
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
    w.writerow(['date','trial time start','stimuli interval (start - stop)','scroll speed','scroll direction','stimulus type'])
else:
    if fsize > 0:
        w = csv.writer(open(f, 'a'), delimiter=',')

#set a phase advancement value
phase_val0 = 0.05
phase_val = phase_val0
#set a factor to change the phase of stimulus by when '-' or '+' is pressed
phase_change = 0.05
#set a factor to change the size of stimulus by when '[' or ']' is pressed
size_change = 5000

#create timers
clock = core.Clock()
interval1pstart = 3    #p for '+' direction
interval1pstop = 60 
interval1mstart = 90    #m for '-' direction
interval1mstop = 120 
interval2pstart = 150 
interval2pstop = 180
interval2mstart = 210 
interval2mstop = 240
interval3pstart = 270
interval3pstop = 300
interval3mstart = 330
interval3mstop = 360
triallength = 390

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
    if clock.getTime() > triallength:
        break
    if interval1pstart<clock.getTime()<interval1pstop : #this creates a never-ending loop
        opto1.setPhase(phase_val, '+')#advance phase by 0.05 of a cycle
        opto1.color -= [0.001, 0.001, 0.001]
        opto1.draw()
        win2.flip()
    w.writerow([d,now,interval1pstop-interval1pstart,phase_val,'+','opto1'])
    if interval1pstop<clock.getTime()<interval1mstart : #this creates a never-ending loop
        win2.flip()
    if interval1mstart<clock.getTime()<interval1mstop : #this creates a never-ending loop
        opto1.setPhase(phase_val, '-')#advance phase by 0.05 of a cycle
        opto1.color -= [0.001, 0.001, 0.001]
        opto1.draw()
        win2.flip()
    w.writerow([d,now,interval1mstop-interval1mstart,phase_val,'-','opto1'])
    if interval1mstop<clock.getTime()<interval2pstart : #this creates a never-ending loop
        win2.flip()
    if interval2pstart<clock.getTime()<interval2pstop : #this creates a never-ending loop
        opto2.setPhase(phase_val, '+')#advance phase by 0.05 of a cycle
        opto2.color -= [0.001, 0.001, 0.001]
        opto2.draw()
        win2.flip()
    w.writerow([d,now,interval2pstop-interval2pstart,phase_val,'+','opto2'])
    if interval2pstop<clock.getTime()<interval2mstart : #this creates a never-ending loop
        win2.flip()
    if interval2mstart<clock.getTime()<interval2mstop : #this creates a never-ending loop
        opto2.setPhase(phase_val, '-')#advance phase by 0.05 of a cycle
        opto2.color -= [0.001, 0.001, 0.001]
        opto2.draw()
        win2.flip()
    w.writerow([d,now,interval2mstop-interval2mstart,phase_val,'-','opto2'])
    if interval2mstop<clock.getTime()<interval3pstart : #this creates a never-ending loop
        win2.flip()
    if interval3pstart<clock.getTime()<interval3pstop : #this creates a never-ending loop
        opto3.setPhase(phase_val, '+')#advance phase by 0.05 of a cycle
        opto3.color -= [0.001, 0.001, 0.001]
        opto3.draw()
        win2.flip()
    w.writerow([d,now,interval3pstop-interval3pstart,phase_val,'+','opto3'])
    if interval3pstop<clock.getTime()<interval3mstart : #this creates a never-ending loop
        win2.flip()
    if interval3mstart<clock.getTime()<interval3mstop : #this creates a never-ending loop
        opto3.setPhase(phase_val, '-')#advance phase by 0.05 of a cycle
        opto3.color -= [0.001, 0.001, 0.001]
        opto3.draw()
        win2.flip()
    w.writerow([d,now,interval3mstop-interval3mstart,phase_val,'-','opto3'])
    if interval3mstop<clock.getTime()<triallength:
        win2.flip()
    if triallength<clock.getTime():
        break

    for key in event.getKeys():
        if key == 'escape':
            triallength = 0
        if key == 'bracketright':
            if interval1pstart<clock.getTime()<interval1mstop :
                opto1.sf += size_change
                opto1.draw()
                win2.flip()
            if interval2pstart<clock.getTime()<interval2mstop :
                opto2.sf += size_change
                opto2.draw()
                win2.flip()
            if interval3pstart<clock.getTime()<interval3mstop :
                opto3.sf += size_change
                opto3.draw()
                win2.flip()
        if key == 'bracketleft':
            if interval1pstart<clock.getTime()<interval1mstop :
                opto1.sf -= size_change
                opto1.draw()
                win2.flip()
            if interval2pstart<clock.getTime()<interval2mstop :
                opto2.sf -= size_change
                opto2.draw()
                win2.flip()
            if interval3pstart<clock.getTime()<interval3mstop :
                opto3.sf -= size_change
                opto3.draw()
                win2.flip()
        if key == 'minus':
            if phase_val - phase_change >= 0:
                if interval1pstart<clock.getTime()<interval1mstop :
                    phase_val -= phase_change
                    opto1.phase = phase_val
                    opto1.draw()
                    win2.flip()
                if interval2pstart<clock.getTime()<interval2mstop :
                    phase_val -= phase_change
                    opto2.phase = phase_val
                    opto2.draw()
                    win2.flip()                
                if interval3pstart<clock.getTime()<interval3mstop :
                    phase_val -= phase_change
                    opto3.phase = phase_val
                    opto3.draw()
                    win2.flip()
            else:
                phase_val = phase_val0
        if key == 'equal':
            if phase_val < 1.00:
                if interval1pstart<clock.getTime()<interval1mstop :
                    phase_val += phase_change
                    opto1.phase = phase_val
                    opto1.draw()
                    win2.flip()
                if interval2pstart<clock.getTime()<interval2mstop :
                    phase_val += phase_change
                    opto2.phase = phase_val
                    opto2.draw()
                    win2.flip()
                if interval3pstart<clock.getTime()<interval3mstop :
                    phase_val += phase_change
                    opto3.phase = phase_val
                    opto3.draw()
                    win2.flip()
            else:
                phase_val = phase_val0

#cleanup
win2.close()
core.quit()
