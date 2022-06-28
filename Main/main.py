from blessings import Terminal
import time
from ascii_mod import *

# Starts with a countdown 
for i in range(5):
    print(f'Starting in {5-i} seconds')
    time.sleep(1)

t = Terminal()
width, height = [0,0]
start = time.time()
while True:
    if [width,height] != [t.width,t.height]:
        clear()
    width, height = [t.width,t.height]
    screenshot()
    with t.location(0, 0):
        print(Ascii(f'./screenshots/Pokemon-0.png',braille=True,threshold=150,dimensions=f'{width - round(width*0.25)},{height - round(height*0.1)}'))
    time.sleep(0.04)
    try:
        os.system('rm ./screenshots/Pokemon-0.png')
    except Exception:
        for i in range(200):
            try:
                os.system(f'rm ./screenshots/Pokemon-{i+1}.png')
            except Exception:
                break
end = time.time()

print(f'Rendered at {1200/(end-start)} frames per second')