__author__ = 'ian'

from psychopy import visual, core, event
import csv
import time
import sys
import os

f = time.strftime('%m%d%Y')+'.csv'
try:
    fsize = os.stat(f).st_size
except OSError:
    w = csv.writer(open(f, 'w'), delimiter=',')
    w.writerow(['species','sex','age','phase','scale','direction'])
else:
    if fsize > 0:
        w = csv.writer(open(f, 'a'), delimiter=',')
try:
    species = sys.argv[1]
except IndexError:
    species = 'unknown'
try:
    sex = sys.argv[2]
except IndexError:
    sex = 'unknown'
try:
    age = sys.argv[3]
except IndexError:
    age = 'unknown'
fullscreen = (1920, 1080)

phase_val = 0.05
scalefactor = 1
scalefactr = 0.01

directionclk = '+'
directioncntr = '-'


dispwin = visual.Window(screen=1, size=fullscreen, pos=(0, 0), monitor="testMonitor", units="deg")

opto1 = visual.GratingStim(win=dispwin, size=fullscreen, pos=[0,0], sf=scalefactor)

direction = directionclk

qu_it = False

while not qu_it:
    #print phase_val
    #print direction
    opto1.setPhase(phase_val, direction)
    opto1.draw()
    dispwin.flip()

    for keyput in event.getKeys():
        if keyput=='o':
            phase_val -= 0.01
            print 'phase = ',phase_val
        if keyput=='p':
            phase_val += 0.01
            print 'phase = ',phase_val
        if keyput=='k':
            opto1.sf -= scalefactr
            print 'scale = ',opto1.sf
        if keyput=='l':
            opto1.sf += scalefactr
            print 'scale = ',opto1.sf
        if keyput=='m':
            direction = directionclk
            print direction,' direction'
        if keyput=='n':
            direction = directioncntr
            print direction,' direction'
        if keyput=='z':
            w.writerow([species,sex,age,str(phase_val),str(opto1.sf[0]),direction])

        if keyput=='q':
            qu_it=True


dispwin.close()
core.quit()