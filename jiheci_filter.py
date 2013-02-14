# -*- coding: utf-8 -*-
import sys

t = {}

of = open('temp.dat', 'w+')

for line in file(sys.argv[1]):
    if line.find('集合词') >= 0:
        of.write(line)

of.close()