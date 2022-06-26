import os
import time

for i in range(10):
    print(f'Starting in {10-i} seconds')
    time.sleep(1)
print('Starting...')
for i in range(1200):
    os.system('xdotool key F12')
    time.sleep(0.0333)
print('Finished')