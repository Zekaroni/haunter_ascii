from blessings import Terminal
import time
from ascii_mod import *
import subprocess as sp

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
        try:
            print(Ascii(f'./screenshots/Pokemon-0.png',color=True,braille=True,threshold=130,dimensions=f'{width - round(width*0.25)},{height - round(height*0.1)}'))
        except Exception:
            print('Waiting 3 seconds due to error')
            time.sleep(3)
            clear()
    time.sleep(0.04)
    try:
        sp.run(['rm ./screenshots/Pokemon-0.png'], check = True)
    except Exception:
        files = sp.getoutput('find ./screenshots -type f -name "*.png"')
        files = files.split('\n')
        for file in files:
            os.system(f'rm {file}')
        
end = time.time()

print(f'Rendered at {1200/(end-start)} frames per second')