import curses
from curses import wrapper
import time
from ascii_mod import *
import subprocess as sp

set_profile(1)


def main(stdscr):
    stdscr.clear()
    for i in range(1200):
        output = open(f'./cache/Pokemon-{i}-ascii-art.txt')
        stdscr.addstr(0,0,output.read())
        stdscr.refresh()
        time.sleep(0.0333)
    stdscr.getch()

wrapper(main)


# sp.getoutput(Ascii(f'./dataset2/Pokemon-0.png',color=True,braille=True,dimensions='10,10',raw=True))