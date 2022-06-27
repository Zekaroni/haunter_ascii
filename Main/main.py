import curses
from curses import wrapper
import time
from ascii_mod import *
import subprocess as sp

def main(stdscr):
    stdscr.clear()
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    
    stdscr.addstr('Hi',curses.color_pair(4))

    stdscr.getch()

wrapper(main)

# sp.getoutput(Ascii(f'./dataset2/Pokemon-0.png',color=True,braille=True,dimensions='10,10',raw=True))