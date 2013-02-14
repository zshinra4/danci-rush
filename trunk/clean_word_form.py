# -*- coding: utf-8 -*-
import sys

t = {}

for line in file(sys.argv[1]):
    line = line.strip()
    x = line.split()
    if len(x) <= 1:
        continue
    for seg in x[1:]:
        y = seg.split('：')
	c = t.get(y[0], 0)
	t[y[0]] = c + 1

of = open('temp.dat', 'w+')

l = [(c,k) for k,c in t.items()]
l.sort(reverse=True)
for c,k in l:
    print >> of, "%s\t%d"%(k,c)