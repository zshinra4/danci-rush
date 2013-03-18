import sys

def is_eng_char(c):
    if c <= 'Z' and c >= 'A' or c<='z' and c>='a':
        return True
    else:
        return False

for line in file(sys.argv[1]):
    x = line.strip().split('###')
    y = x[1].decode('utf-8')
    is_error = False
    s = ''
    for idx in range(len(y)-1):
        s += y[idx].encode('utf-8')
        idx2 = idx+1
        if is_eng_char(y[idx]) and (y[idx2] == ',' or y[idx2] == '/' or y[idx2] == '-'):
	    pass
	elif is_eng_char(y[idx]) and not is_eng_char(y[idx2]):
	    is_error = True
	    s += ','
    if len(y) > 0:
        s += y[len(y)-1].encode('utf-8')
    x[1] = s
    print '###'.join(x)
    '''
    if is_error:
        print line.strip()
    '''
