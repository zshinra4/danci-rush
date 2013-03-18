import sys

t = {}

for line in file(sys.argv[1]):
    x = line.strip().split('###', 1)
    w = x[0]
    if w in t:
        old_len = len(t[w])
	if len(x[1]) > old_len:
	    t[w] = x[1]
    else:
        t[w] = x[1]

l = [(w.lower(), w ,cnt) for w,cnt in t.items()]
l.sort()

for w,w2,cnt in l:
    print "%s###%s"%(w2,cnt)
