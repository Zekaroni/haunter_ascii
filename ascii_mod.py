import os

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

def set_profile(profile):
    os.system(f'xdotool key shift+F10 r {profile}')