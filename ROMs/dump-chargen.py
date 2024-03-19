#!/usr/bin/python3
#
# Dump the Microbee character generator ROM to a PNG.
#
# Input:  Main-Board-IC13.bin
# Output: character-set.png

import io
import sys
from PIL import Image

with open('Main-Board-IC13.bin', 'rb') as file:
    file_data = file.read()

image = Image.new('RGB', (8 * 16 * 2, 8 * 16 * 2))
for ch in range(128):
    for y in range(16):
        bits = file_data[ch * 16 + y]
        for x in range(8):
            if (bits & (0x80 >> x)) != 0:
                px = ((ch % 16) * 8 + x) * 2
                py = ((ch & 0xF0) + y) * 2
                image.putpixel((px, py), (0, 255, 0))
                image.putpixel((px + 1, py), (0, 255, 0))
                image.putpixel((px, py + 1), (0, 255, 0))
                image.putpixel((px + 1, py + 1), (0, 255, 0))
                image.putpixel((px, py), (0, 255, 0))

image.save('character-set.png')
