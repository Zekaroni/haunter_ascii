import time
import subprocess as sp
import os

# Tries to locate packages, if unable, ask user for consent to download
try:
    sp.check_output('ascii-image-converter')
    import PIL
    from blessed import Terminal
    from pyboy import PyBoy,logger,WindowEvent
except Exception:
    cons = input('Packages that are not installed are needed for this to run; Would you like to install them? (y/n) : ')
    if cons == 'y':
        try:
            sp.check_output('ascii-image-converter')
        except Exception:
            os.system('sudo snap install ascii-image-converter')
        try:
            import PIL
        except Exception:
            os.system('pip install pillow')
            import PIL
        try:
            from blessed import Terminal
        except Exception:
            os.system('pip install blessed')
            from blessed import Terminal
        try:
            from pyboy import PyBoy,logger,WindowEvent
        except Exception:
            os.system('pip install pyboy')
            from pyboy import PyBoy,logger,WindowEvent
    else:
        print('Unable to start without needed packages\nExiting...')
        exit()

#

# Disables logging
logger.log_level("DISABLE")

A = 'j'; B = 'k'; UP = 'w'; DOWN = 's'; LEFT = 'a'; RIGHT = 'd'; START = 'u'; SELECT = 'i'; SAVE = '5' ; CLOSE = 'q'

# Sets the game file based on path input
game_file = './tmp/Pokemon - Red.gb'
# Leaving blank will search files and children of local folder for a save, if none is found it will create one ; Can be replaced with save location
save_file = ''

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

# Initializes the emulator
pyboy = PyBoy(game_file,window_type='headless')

# Creates a terminal object
t = Terminal()

# # # Misc Functions

def Ascii(image,color=False,dimensions=None,braille=False,dither=False,threshold=False,custom=False,full=False,save=False,bg_color=False,raw=False,complex=False):
    input = ''
    if color:
        input += ' -C'
    if dimensions:
        input += f' -d {dimensions}'
    if braille:
        input += ' -b'
        if dither:
            input += f' --dither'
        if threshold:
            input += f' --threshold {threshold}'
    if custom:
        input += f' -m "{custom}"'
    if full:
        input += ' -f'
    if save:
        input += f' --save-txt {save} --only-save'
    if bg_color:
        input += ' --color-bg'
    if complex:
        input += ' -c'
    if raw:
        return f'ascii-image-converter {image}{input}'
    else:
        os.system(f'ascii-image-converter {image}{input}')

def clear():
    os.system('clear')

def print0(str,line=False,timeout=False):
    if line:
        with t.location(0,0):
            print('-'*(t.width-padx),end='')
    with t.location(0,0):
        print(str,end='')
    if timeout:
        time.sleep(timeout)

def pause(*args,line=False,cls=True,cusp=False):
    if cls:
        clear()
    if args:
        for arg in args:
            if cusp:
                print0(arg,line=line)
            else:
                print(arg)
    input()

# # # Emulator functions

def game_input(key,state):
    global prev_key
    # Press
    if state == 0:
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
    # Release
    elif state == 1:
        for button in CONTROLS:
            if key == CONTROLS[CONTROLS.index(button)][0]:
                release = CONTROLS[CONTROLS.index(button)][2]
        try:
            pyboy.send_input(release)
        except Exception:
            pass

def save_game(pass_check=False):
    global save_file
    if pass_check:
        save = open(save_file,'wb')
        pyboy.save_state(save)
    else:
        print0('Are you sure you want to save the game? (y/n)',line=True)
        choice = t.getch()
        if choice == 'y':
            print0('Saving the game',line=True)
            time.sleep(1)
            save = open(save_file,'wb')
            pyboy.save_state(save)
            print0('Game has been saved',line=True)
            time.sleep(1)

def load_game():
    global save_file
    try:
        print0('Would you like to load the save? (y/n)', line=True)
        choice = t.getch()
        if choice == 'y':
            save = open(save_file,'rb')
            pyboy.load_state(save)
    except Exception:
        pass

def init_save():
    global save_file
    if save_file == '':
        for obj in os.listdir('.'):
            if os.path.isfile(os.path.join('.', obj)):
                if obj == 'save.state':
                    save_file = os.path.join('.',obj)
                    break
            else:
                new_path = os.path.join('.',obj)
                for obj2 in os.listdir(new_path):
                    if os.path.isfile(os.path.join(new_path, obj2)):
                        if obj2 == 'save.state':
                            save_file = os.path.join(new_path, obj2)
                            break
        if save_file == '':
            save_file = './save.state'
            save_game(pass_check=True)
        else:
            save = open(save_file,'rb')
            pyboy.load_state(save)
    else:
        try:
            save = open(save_file,'rb')
            pyboy.load_state(save)
        except Exception:
            print0("The save file you entered either doesn't exist or was entered wrong\n"
            "Closing in 5 seconds",timeout=5)
            clear()
            exit()
        
# # # Mian script

def main():
    global width,height,prev_key,current_key
    clear()
    pyboy.tick()
    init_save()

    # Runs while the emulator can progress a "tick"
    while not pyboy.tick():
        # Checks if a key is being pressed, if true, it does the in-game action
        if t.kbhit(timeout=0):
            current_key = t.getch()
            if current_key == prev_key:
                pass
            elif current_key == SAVE:
                save_game()
            elif current_key == CLOSE:
                clear()
                exit()
            else:
                game_input(current_key,0)
                prev_key = current_key
        elif current_key != '':
            game_input(current_key,1)
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
        print0(sp.getoutput(Ascii('./tmp/pkmtmp.png',braille=True,dimensions=f'{width - pady},{height - padx}',raw=True)))
    # Stops the emulator if tick can no longer be updated
    pyboy.stop()

with t.cbreak(),t.hidden_cursor():
    main()