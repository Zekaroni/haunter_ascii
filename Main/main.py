from blessings import Terminal
import time
from ascii_mod import *
from pyboy import PyBoy

# Starts with a countdown 
for i in range(5):
    print(f'Starting in {5-i} seconds')
    time.sleep(1)

pyboy = PyBoy('./Pokemon - Red Version.gb')
t = Terminal()
width, height = [0,0]

while not pyboy.tick():
    pyboy.screen_image().save('./tmp/pkmtmp.png')
    if [width,height] != [t.width,t.height]:
        clear()
    width, height = [t.width,t.height]
    with t.location(0, 0):
        print(Ascii('./tmp/pkmtmp.png',braille=True,threshold=150,dimensions=f'{width - round(width*0.25)},{height - round(height*0.1)}'))
pyboy.stop()