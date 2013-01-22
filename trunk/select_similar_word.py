# -*- coding: utf-8 -*-

import sys
import string

def intersect(t1,t2):
    cnt = 0
    for k,v in t1.items():
        if k in t2:
	    cnt += 1
    return cnt

class sense:
    def __init__(self):
        self.type = ''
	self.cnt = ''
	self.tbl = {}
	self.tbl_init = False
    def get_tbl(self):
        if not self.tbl_init:
	    x = self.cnt.decode('UTF-8')
	    for i in x:
	        self.tbl[i] = 1
	    self.tbl_init = True
	return self.tbl
    def similar(self, s):
        t1 = self.get_tbl()
	t2 = s.get_tbl()
	if len(t1) == 0 or len(t2) == 0:
	    return 0.0
	ret = intersect(t1, t2)
	return ret*1.0/min(len(t1), len(t2))

def segment(s):
    s = string.replace(s, '；', ' ')
    s = string.replace(s, '，', ' ')
    s = string.replace(s, ';', ' ')
    s = string.replace(s, ',', ' ')
    return s.split()

class word:
    def __init__(self):
        self.cnt = ''
        self.sense_list = []
    def read_from_line(self, line):
        sgms = line.strip().split('###')
	self.cnt = sgms[0]
	for sgm in sgms[2:]:
	    y = sgm.split('.')
	    if len(y) < 2:
	        continue
	    z = segment(y[1])
	    for i in z:
	        if i == '&amp':
		    continue
	        s = sense()
	        s.type = y[0]
	        s.cnt = i
	        self.sense_list.append(s)
    def dump(self, fp):
        toprint = []
	toprint.append(self.cnt)
        for s in self.sense_list:
	    toprint.append(s.type+":"+s.cnt)
	    #toprint.append(s.type)
	fp.write("%s\n"%','.join(toprint))

    def similar(self, w):
        if self.cnt == w.cnt:
	    return ''
	similar_string = ''
        for i in self.sense_list:
	    for j in w.sense_list:
	        if i.type != j.type:
		    continue
		score = i.similar(j)
		if score > 0.5:
		    similar_string = "%s,%s,%s,%.4g"%(i.type,i.cnt,j.cnt, score)
		    break
	    if len(similar_string) > 0:
	        similar_string = w.cnt + ',' + similar_string
	        break
	return similar_string


	        

word_table = []

fp = file('temp.dat', 'w+')
for line in file(sys.argv[1]):
    w = word()
    w.read_from_line(line)
    w.dump(fp)
    word_table.append(w)
fp.close()

fp = file('similar_words.dat', 'w+')
for i_idx in range(len(word_table)):
    i = word_table[i_idx]
    i_list = []
    for j_idx in range(i_idx+1,len(word_table)):
        j = word_table[j_idx]
        s = i.similar(j)
	if len(s) > 0:
	    i_list.append(s)
    if len(i_list) > 0:
        fp.write("%s\t%s\n"%(i.cnt, '\t'.join(i_list)))
    #if i_idx  > 10:
    #    break
fp.close()