from blessed import Terminal
from ascii_mod import *
from pyboy import PyBoy,logger,WindowEvent
import time
import subprocess as sp

A = 'j'
B = 'k'
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
START = 'u'
SELECT = 'i'
SAVE = '5'

# Disables logging
logger.log_level("DISABLE")

# Initializes the emulator
pyboy = PyBoy('./tmp/Pokemon - Red.gb',window_type='headless')

# Creates a terminal object
t = Terminal()

# Initializes needed variables
padx, pady  = 2 ,2
width, height = [0,0]
press,release,prev_key,current_key = '','','',''
CONTROLS = [
    [A,WindowEvent.PRESS_BUTTON_A,WindowEvent.RELEASE_BUTTON_A],
    [B,WindowEvent.PRESS_BUTTON_B,WindowEvent.RELEASE_BUTTON_B],
    [UP,WindowEvent.PRESS_ARROW_UP,WindowEvent.RELEASE_ARROW_UP],
    [DOWN,WindowEvent.PRESS_ARROW_DOWN,WindowEvent.RELEASE_ARROW_DOWN],
    [LEFT,WindowEvent.PRESS_ARROW_LEFT,WindowEvent.RELEASE_ARROW_LEFT],
    [RIGHT,WindowEvent.PRESS_ARROW_RIGHT,WindowEvent.RELEASE_ARROW_RIGHT],
    [START,WindowEvent.PRESS_BUTTON_START,WindowEvent.RELEASE_BUTTON_START],
    [SELECT,WindowEvent.PRESS_BUTTON_SELECT,WindowEvent.RELEASE_BUTTON_SELECT]
]

def game_input(key,state):
    global prev_key
    if state == 'press':
        for button in CONTROLS:
            # Checks to see if key pressed is in CONTROLS
            if key == CONTROLS[CONTROLS.index(button)][0]:
                press = CONTROLS[CONTROLS.index(button)][1]
            if key == CONTROLS[CONTROLS.index(button)][0]:
                release = CONTROLS[CONTROLS.index(button)][2]
        try:
            pyboy.send_input(release)
            pyboy.send_input(press)
        except Exception:
            pass
    elif state == 'release':
        for button in CONTROLS:
            if key == CONTROLS[CONTROLS.index(button)][0]:
                release = CONTROLS[CONTROLS.index(button)][2]
        try:
            pyboy.send_input(release)
        except Exception:
            pass

def print0(str):
    with t.location(0,0):
        print(str,end='')

def save_game():
    print0('-'*(t.width-padx))
    print0('Are you sure you want to save the game? (y/n)')
    choice = t.getch()
    if choice == 'y':
        print0('-'*(t.width-padx))
        print0('Saving the game')
        time.sleep(1)
        save = open('./tmp/save.state','wb')
        pyboy.save_state(save)
        print0('-'*(t.width-padx))
        print0('Game has been saved')
        time.sleep(1)

def main():
    global width,height,prev_key,current_key
    clear()
    pyboy.set_emulation_speed(2)
    try:
        # Load save file if there is one
        save = open('./tmp/save.state','rb')
        pyboy.load_state(save)
        clear()
        print0('Loading save...')
        time.sleep(1)
    except:
        # Starts a new game if no save file is found
        print0('No file found, starting a new game...')
        time.sleep(1)
    # Runs while the emulator can progress a "tick"
    while not pyboy.tick():
        # Checks if a key is being pressed, if true, it does the in-game action
        if t.kbhit(timeout=0):
            current_key = t.getch()
            if current_key == prev_key:
                pass
            elif current_key == SAVE:
                save_game()
            else:
                game_input(current_key,'press')
                prev_key = current_key
        elif current_key != '':
            game_input(current_key,'release')
            current_key = ''
        else:
            prev_key = ''
        # Checks window size, if different, it clears
        if [width,height] != [t.width,t.height]:
            clear()
        # Sets width and height of current terminal size
        width, height = [t.width,t.height]
        # Captures current frame
        pyboy.screen_image().save('./tmp/pkmtmp.png')
        # Displays current frame in ASCII in terminal
        print0(sp.getoutput(Ascii('./tmp/pkmtmp.png',threshold=170,braille=True,dimensions=f'{width - pady},{height - padx}',raw=True)))
    # Stops the emulator if tick can no longer be updated
    pyboy.stop()

with t.cbreak(),t.hidden_cursor():
    main()