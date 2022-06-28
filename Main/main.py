import curses
from curses import color_content, wrapper
from ascii_mod import *

set_profile(1)


def main(stdscr):
    stdscr.clear()
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    for i in range(1200):
        stdscr.move(0, 0)
        chars = decode(f'./dataset/Pokemon-{i}.png')
        final_pixels = []
        for char in chars:
            color = xterm(char[0])
            final_pixels.append([color,char[1]])
        for pixel in final_pixels:
            stdscr.addstr(f'{pixel[1]}',curses.color_pair(pixel[0]))
        stdscr.refresh()

    stdscr.getch()

wrapper(main)