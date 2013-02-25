# -*- coding: utf-8 -*-

import sys

of = open("temp.dat", 'w+')

t = {}

for line in file(sys.argv[1]):
    x = line.strip().split('###')
    for _means in x[3:]:
        means = _means.replace('&amp', '').replace('，',',').replace('；',';').replace(',',';')
	if means.startswith('vt.') or means.startswith('vi.') or means.startswith('v.'):
	    means = means.replace('vt.', '').replace('vi.', '').replace('v.', '')
	    y = means.split(';')
	    for i in y:
	        if len(i) == 0:
		    continue
		if i not in t:
		    t[i] = []
		t[i].append(x[0])

for k,l in t.items():
    of.write("%s\t%s\n"%(k,"\t".join(l)))

of.close()