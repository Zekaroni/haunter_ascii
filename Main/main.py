from blessings import Terminal
import time
import subprocess as sp
from ascii_mod import *

t = Terminal()
width, height = [0,0]
start = time.time()
for i in range(1200):
    if [width,height] != [t.width,t.height]:
        clear()
    width, height = [t.width,t.height]
    output = sp.getoutput(Ascii(f'./dataset/Pokemon-{i}.png',braille=True,threshold=155,dimensions=f'{width - round(width*0.25)},{height - round(height*0.1)}',raw=True))
    with t.location(0, 0):
        print(output)
    time.sleep(0.0167)
end = time.time()

print(f'Rendered at {1200/(end-start)} frames per second')