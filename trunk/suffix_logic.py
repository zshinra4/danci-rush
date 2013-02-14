import sys

t3 = {}
t4 = {}
t3_word = {}
t4_word = {}

for line in file(sys.argv[1]):
    x = line.strip().split('###')
    if len(x) > 0 and len(x[0]) >= 4:
        s3 = x[0][-3:]
	s4 = x[0][-4:]
	c = t3.get(s3,0)
	t3[s3] = c + 1
	c = t4.get(s4,0)
	t4[s4] = c + 1
	if s3 not in t3_word:
	    t3_word[s3] = []
	if s4 not in t4_word:
	    t4_word[s4] = []
	t3_word[s3].append(x[0])
	t4_word[s4].append(x[0])

of = open('temp.dat', "w+")

l = []
for k,c in t3.items():
    if c >= 3:
        l.append((c,k))
    l.sort(reverse=True)
for a,b in l:
    of.write("%s\t%d\t%s\n"%(b,a,','.join(t3_word[b])))

l = []
for k,c in t4.items():
    if c >= 3:
        l.append((c,k))
    l.sort(reverse=True)
for a,b in l:
    of.write("%s\t%d\t%s\n"%(b,a,','.join(t4_word[b])))
of.close()