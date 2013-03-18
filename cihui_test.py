import datetime
import sys
import os
#import msvcrt

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()
    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

platform_getch = _Getch()


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

selector = ''
for i in sys.argv:
    if i.startswith('selector:'):
        a,b = i.split(":")
        selector = b
        print "[INFO] set selector: %s"%selector
	break

idx = 0
while 1:
    if len(selector) > 0:
        last_state = state_list[idx].split()[-1]
        if last_state != selector:
	    state_list[idx]+=(" "+last_state)
	    idx += 1
	    continue

    print word_list[idx]
    #ch = sys.stdin.read(1)
    #ch = msvcrt.getch()
    ch = platform_getch()
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
