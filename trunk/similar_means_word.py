# -*- coding: utf-8 -*-
import sys
import re

re_branket = re.compile(r'(\[[^\]]+\])|(（[^）]+）)|(〈[^〉]+〉)|(〔[^〕]+〕)|(\([^\)]+\)|(\<[^\>]+\>))'.decode('utf8'), re.UNICODE)
re_split = re.compile(r'[;；,，]'.decode('utf8'), re.UNICODE)

'''
format:
word###forms###pronounciation###means-list
'''


def clear_means(s):	
    s2 = re_branket.sub(r'', s.decode('utf8')).encode('utf8')

    idx = s2.rfind('.')
    state = ''
    if idx >= 0:
       	state = s2[:idx]
        s2 = s2[idx+1:]
    state = state.replace('&amp', '&')
    
    s3 = re_split.split(s2.decode('utf8'))
    s4 = [i.encode('utf8') for i in s3]
    

    return state, s4
    
tbl = {}

for line in file(sys.argv[1]):
    x = line.strip().split('###')
    w = x[0].lower()
    for i in x[3:]:
        state,l = clear_means(i)
	for m in l:
	    if m == '':
	        continue
	    if m not in tbl:
	        tbl[m] = []
	    tbl[m].append("%s.%s"%(w, state))

of = open('tmp.dat', 'w+')
output_l = []
for m,l in tbl.items():
    output_l.append((len(l),m,l))

output_l.sort(reverse=True)
for cnt,m,l in output_l:
    s = "%s\t[%d]\t%s"%(m, cnt, '\t'.join(l))
    of.write("%s\n"%s)
of.close()     

stat_t = {}
for m,l in tbl.items():
    cnt = len(l)
    c = stat_t.get(cnt, 0)
    stat_t[cnt] = c + 1

l = [(freq,cnt) for cnt,freq in stat_t.items()]
l.sort(reverse=True)
for freq,cnt in l:
    print "f:%d\tc:%d"%(freq,cnt)