import sys

sense_t = []
form_t = {}

of = file("kaoyan_merge_words.dat", "w+")

for line in file(sys.argv[1]):
    x = line.strip().split('###', 1)
    sense_t.append((x[0], x[1]))

for line in file(sys.argv[2]):
    x = line.strip().split()
    if len(x) == 0:
        continue
    if len(x) <= 1:
        form_t[x[0]] = "NONE"
    else:
        form_t[x[0]] = ','.join(x[1:])
    
for w,sense in sense_t:
    form_string = form_t.get(w, 'NONE')
    print >> of, "%s###%s###%s"%(w, form_string, sense)