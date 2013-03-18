# -*- coding: utf-8 -*-

import sys

for line in file(sys.argv[1]):
    x = line.strip().split('###')
    y = x[1].split(',')
    t = {}
    for i in y:
        if i == 'NONE':
	    continue
        try:
            k,v = i.split('：')
	except:
	    print "[ERROR]\t[%s]\t%s"%(x[0],i)
	    continue
	t[k] = v
    if '第三人称单数' in t and t['第三人称单数'] == x[0]:
        print line.strip()
    
