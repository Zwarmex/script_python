#! /usr/bin/python

nbr_row = input("How many rows do you want ?\n=> ")
max_space = int(nbr_row)*2-1


for i in range(1, int(nbr_row) + 1):
    nbr_stars = i*2-1
    blank = max_space-nbr_stars
    space = blank//2
    print(" {0}{1}{0}".format(' ' * space, '*' * nbr_stars))
    