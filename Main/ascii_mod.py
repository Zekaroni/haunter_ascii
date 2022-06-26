import os
import time

def Ascii(image,color=False,dimensions=None,braille=False,full=False,save=False,bg_color=False,raw=False):
    input = ''
    if color:
        input += ' -C'
    if dimensions:
        input += f' -d {dimensions}'
    if braille:
        input += ' -b'
    if full:
        input += ' -f'
    if save:
        input += f' --save-txt {save} --only-save'
    if bg_color:
        input += ' --color-bg'
    if raw:
        return f'ascii-image-converter {image}{input}'
    else:
        os.system(f'ascii-image-converter {image}{input}')

def clear():
    os.system('clear')

def set_profile(profile):
    os.system(f'xdotool key shift+F10 r {profile}')
#&& xdotool key ctrl+shift+a