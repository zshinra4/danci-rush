def editorial_distance(x, y):
    if len(x) == 0:
        return len(y)

    if len(y) == 0:
        return len(x)
    
    if x[0] == y[0]:
        return editorial_distance(x[1:],y[1:])
    else:
        #change x[0]
	change_step = 1 + editorial_distance(x[1:], y[1:])

	#delete x[0]
	delete_step = 1 + editorial_distance(x[1:], y)

	#add x[0]
	add_step = 1 + editorial_distance(x, y[1:])
	
	return min([change_step, delete_step, add_step])


def editorial_distance2(x, y, xi, yi):
    lx = len(x)
    ly = len(y)

    if xi >= lx:
        return ly - yi

    if yi == ly:
        return lx - xi
    
    if x[xi] == y[yi]:
        return editorial_distance2(x,y, xi+1, yi+1)
    else:
        #change x[0]
	change_step = 1 + editorial_distance2(x, y, xi+1, yi+1)

	#delete x[0]
	delete_step = 1 + editorial_distance2(x, y, xi+1, yi)

	#add x[0]
	add_step = 1 + editorial_distance2(x, y, xi, yi+1)
	
	return min([change_step, delete_step, add_step])


tmpx=[]
for i in range(100):
    tmpx.append([0 for i in range(100)])

def editorial_distance3(x,y):
    _l = list(x+"\x01"); _l.reverse()
    _x = ''.join(_l)
    _l = list(y+"\x01"); _l.reverse()
    _y = ''.join(_l)

    lx = len(_x)
    ly = len(_y)
    assert lx < 100
    assert ly < 100

    print _x
    print _y

    for i in range(lx):
        tmpx[i][0] = 0
    for j in range(ly):
        tmpx[0][j] = 0
    
    for xi in range(lx):
        if xi == 0:
	    continue
        for yi in range(ly):
	    if yi == 0:
	        continue

	    m = min([tmpx[xi-1][yi-1], tmpx[xi-1][yi], tmpx[xi][yi-1]])
	    if _x[xi] == _y[yi]:
	        tmpx[xi][yi] = m
	    else:
	        tmpx[xi][yi] = m + 1

    return tmpx[lx-1][ly-1]
   
print editorial_distance3("prgres", "prograss")
print editorial_distance2("prgres", "prograss", 0, 0)
print editorial_distance("prgres", "prograss")

'''
fp = file("danci.txt")
l = [ln.strip() for ln in fp]

limit = len(l)

for i in range(limit):
    knn = []
    if len(l[i]) == 0:
        continue

    for j in range(limit):
        if i != j and len(l[j]) > 0:
	    print "[%s] vs [%s]"%(l[i], l[j])
	    d = editorial_distance2(l[i], l[j], 0, 0)
	    if d <= 2:
	        knn.append((d, l[j]))

    knn.sort()
    
    outputs = "%s\t%s"%(l[i], "\t".join([str(x[1]) for x in knn[:10]]))
    print outputs
'''