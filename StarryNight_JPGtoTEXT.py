# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:03:20 2018

@author: jlewin

JPEG to Text and Blocks

using source code found at: http://nbviewer.jupyter.org/github/jiffyclub/ipythonblocks/blob/master/demos/starry_night_to_text.ipynb
"""

from PIL import Image
im = Image.open('StarNight.jpg')
im.size

im = im.resize((125, 100), Image.ANTIALIAS)

#Getdata() method gives an iterable sequence of RGB tuples starting at the top left image pixel and going down row by row

imdata = im.getdata()

#organize data structures
import os
import itertools
with open('starry_night.txt', 'w') as f:
    s = ['# width height', '{0} {1}'.format(im.size[0], im.size[1]),
         '# block size', '4',
         '# initial color', '0 0 0',
         '# row column red green blue']
    f.write(os.linesep.join(s) + os.linesep)
    
    for ((row, col), colors) in zip(itertools.product(range(im.size[1]), range(im.size[0])), imdata):
        things = [str(x) for x in (row, col) + colors]
        f.write(' '.join(things + ['\n']))






from ipythonblocks import BlockGrid
grid = BlockGrid(125, 100, block_size=4, lines_on =False)
for block, colors in zip(grid, imdata):
    block.rgb = colors
grid    