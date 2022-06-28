from ascii_mod import *
import subprocess as sp


output = sp.getoutput(Ascii(f'./dataset/Pokemon-0.png',color=True,braille=True,dimensions='300,100',bg_color=True,raw=True))

new = output.split('[48;2;')
thing = []
for value in new:
    thing.append(value.replace('\x1b[0m',''))

for line in thing:
    print(line)