#!/usr/bin/env python3

from PIL import Image

imagenm = input("Type the name of your image: ")

print(imagenm)

im = Image.open(imagenm)

pix = im.load()

w,h = im.size

x = 0
y = 0

print(x+1,y+1, pix[x,y])


while (x<w) and (y<h):
	y += 1
	print(x+1,y+1, pix[x,y])
	if y==h-1:
		x += 1
		y = 0