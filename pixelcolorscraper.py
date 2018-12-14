#!/usr/bin/env python3

from PIL import Image

imagenm = input("Type the name of your image: ")

filecheck = input("Do you want to output the results to a file instead? (y/n) ")

im = Image.open(imagenm)

pix = im.load()

w,h = im.size

x = 0
y = -1

if filecheck == 'y':
	filename = input("What is the file name? ")
	while (x<w) and (y<h):		
		y += 1
		print(x,y, pix[x,y], file = open(filename, "a"))
		if y==h-1:
			x += 1
			y = -1
else:
	while (x<w) and (y<h):
		y += 1
		print(x,y, pix[x,y])
		if y==h-1:
			x += 1
			y = -1