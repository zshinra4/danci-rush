import sys

l = []
for line in file(sys.argv[1]):
    x = line.strip().split('###')
    l.append((x[0].lower(), x[0], x[1]))

l.sort()

for w1,w,cnt in l:
    print "%s###%s"%(w,cnt)
