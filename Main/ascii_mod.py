import os
import time
from PIL import Image

def get_rgb(file,xterm=False):
    img = Image.open(file).convert('RGB')
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
        return colors
    else:
        return pixels

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

for pixel in get_rgb('./dataset/Pokemon-0.png'):
    r, g, b = pixel
    color = round((r*6/256)*36 + (g*6/256)*6 + (b*6/256))