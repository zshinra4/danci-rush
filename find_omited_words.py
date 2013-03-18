import sys
t1 = {}
for line in file(sys.argv[1]):
    x = line.strip().lower()
    t1[x] = 1

t2 = {}
for line in file(sys.argv[2]):
    x = line.strip().split('###', 1)
    t2[x[0].lower()] = 1

for k,v in t1.items():
    if k not in t2:
        print k
