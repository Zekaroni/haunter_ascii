import os
from PIL import Image
import subprocess as sp

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

def get_rgb(file,xterm=False,get_size=False):
    img = Image.open(file).convert('RGB')
    width, height = img.size
    img = img.resize((round(width/2),round(height/2)))
    data = img.getdata()
    pixels = []
    for cluster in data:
        pixels.append(cluster)
    if xterm:
        colors = []
        for pixel in pixels:
            r, g, b = pixel
            color = round((r*6/256)*36 + (g*6/256)*6 + (b*6/256))
            colors.append(color)
        if get_size:
            width, height = img.size
            return [width, height, colors]
        else:
            return colors
    else:
        return pixels

def decode(file):
    output = sp.getoutput(Ascii(f'{file}',color=True,braille=True,dimensions='300,100',bg_color=True,raw=True))

    values = output.split('[48;2;')
    decoded = []
    cycle = 0
    for value in values:
        split = value.replace('\x1b[0m','').split('m')
        try:
            decoded.append([split[0].split(';'),split[1]])
        except Exception:
            pass
        cycle+=1
    return decoded

def xterm(rgb):
    r,g,b = rgb
    color = round((int(r)*6/256)*36 + (int(g)*6/256)*6 + (int(b)*6/256))
    return color

def clear():
    os.system('clear')

def set_profile(profile):
    os.system(f'xdotool key shift+F10 r {profile}')