import curses
from curses import color_content, wrapper
from doctest import OutputChecker
import time
from ascii_mod import *
import subprocess as sp
import culour

set_profile(1)

def main(stdscr):
    global output
    stdscr.clear()
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    output = []

    file = open('./cache/Pokemon-0-ascii-art.txt','r').read()

    for char in file:
        output.append(char)
        try:
            curses.addstr(char)
        except Exception:
            pass
    
    stdscr.getch()

wrapper(main)

for line in output:
    print(line)