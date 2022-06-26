from ascii_mod import *


for i in range(1200):
    Ascii(f'./dataset/Pokemon-{i}.png',braille=True,save='./cache',dimensions='300,100')








# import subprocess as sp

# set_profile(1)

# output = sp.getoutput(Ascii(f'./dataset2/Pokemon-0.png',color=True,braille=True,dimensions='300,100',bg_color=True,raw=True))
# print (output)

# set_profile(1)

# f = open('Pokemon-0-ascii-art.txt')
# print(f.read())

# set_profile(1)
# for i in range(1200):
#     if i % 10 == 0:
#         clear()
#     Ascii(f'./dataset2/Pokemon-{i}.png',color=True,dimensions='320,100',braille=True)