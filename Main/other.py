from ascii_mod import *
import subprocess as sp


# output = sp.getoutput(Ascii(f'./dataset/Pokemon-0.png',color=True,braille=True,dimensions='300,100',bg_color=True,raw=True))
# print(output)

file = open('test.txt','r')
print(file.read())

# for i in range(1200):
#     Ascii(f'./dataset/Pokemon-{i}.png',braille=True,save='./cache',dimensions='300,100')



# # # Curses
  # for i in range(0, 255):
    #     stdscr.addstr(str(i), curses.color_pair(i))
    # stdscr.refresh()
    
    # for i in range(1200):
    #     output = open(f'./cache/Pokemon-{i}-ascii-art.txt')
    #     stdscr.addstr(0,0,output.read())
    #     stdscr.refresh()
    #     time.sleep(0.0333)

# import subprocess as sp

# set_profile(1)

# output = sp.getoutput(Ascii(f'./dataset2/Pokemon-0.png',color=True,braille=True,dimensions='300,100',bg_color=True,raw=True))
# print (output)


# for i in range(1200):
    #     output = open(f'./cache/Pokemon-{i}-ascii-art.txt')
    #     stdscr.addstr(0,0,output.read())
    #     stdscr.refresh()
    #     time.sleep(0.0333)

    # width,height,pixels = get_rgb(
    #     './dataset/Pokemon-0.png',xterm=True,get_size=True)

    # output = []

    # line = 0
    # pos = 0
    # cycle = 0
    # for color in pixels:
    #     if (cycle+1) % width == 0:
    #         line += 1
    #     if (cycle+1) % height == 0:
    #         pos = 0
    #     try:
    #         output.append([line,pos])
    #         stdscr.addstr(line,pos,' ',curses.color_pair(int(color)) | curses.A_REVERSE)
    #     except curses.error:
    #         output.append(f'Error on cycle {cycle}')
    #     pos+=1
    #     cycle+=1



# set_profile(1)

# f = open('Pokemon-0-ascii-art.txt')
# print(f.read())

# set_profile(1)
# for i in range(1200):
#     if i % 10 == 0:
#         clear()
#     Ascii(f'./dataset2/Pokemon-{i}.png',color=True,dimensions='320,100',braille=True)