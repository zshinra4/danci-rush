import datetime
import sys
import os
import msvcrt

word_list = [l.strip() for l in file("danci.txt") if len(l) > 0]
jieshi_list = [l.strip() for l in file("jieshi.txt") if len(l) > 0]
state_list = [l.strip() for l in file("state.txt") if len(l) > 0]

if len(state_list) < len(word_list):
    state_list = []
    for i in range(len(word_list)):
        state_list.append(word_list[i]+"\t\t\t")

print "wl.len=%d js.len=%d"%(len(word_list), len(jieshi_list))
print "ENTER:know U:unknown N:uncertainty"

know_c = 0
unknow_c = 0
uncertainty_c = 0

def report():
    print "know: %d"%know_c
    print "unknow: %d"%unknow_c
    print "uncertainty: %d"%uncertainty_c

def rewrite_state():
    sfp = file("state.txt", "w+")
    for i in state_list:
        sfp.write(i+"\n")

idx = 0
while 1:
    print word_list[idx]
    #ch = sys.stdin.read(1)
    ch = msvcrt.getch()
    if ch == '\r':
        know_c += 1
	state_list[idx] += " K"
    elif ch == 'n':
        uncertainty_c += 1
	state_list[idx] += " N"
    elif ch == 'u':
        unknow_c += 1
	state_list[idx] += " U"
    elif ch == 'q':
        os._exit(0)
    else:
        continue

    idx += 1
    if idx >= len(word_list):
        print "test finished!"
	rewrite_state()
	report()
	os._exit(0)