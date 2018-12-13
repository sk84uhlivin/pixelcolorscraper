#!/usr/bin/env python3

from PIL import Image

imagenm = input("Type the name of your image: ")

file = input("Do you want to output the results to a .txt instead? ")

im = Image.open(imagenm)

pix = im.load()

w,h = im.size

x = 0
y = 0

print(x,y, pix[x,y], file = open("list.txt", "a"))

while (x<w) and (y<h):
	if file == 'y':
		y += 1
		print(x,y, pix[x,y], file = open("list.txt", "a"))
		if y==h-1:
			x += 1
			y = 0
	else:
		y += 1
		print(x,y, pix[x,y])
		if y==h-1:
			x += 1
			y = 0