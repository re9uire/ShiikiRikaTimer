# coding: utf-8
import time

a = 0
b = 0
c = 0
d = 0

while True:
    print "[ %s : %s : %s : %s ]:椎木里佳." %(str(a),str(b),str(c),str(d))
    d += 1
    time.sleep(0.01)
    if d > 99:
        d = 0
        c += 1
    if c > 59:
        c = 0
        b += 1
    if b > 59:
        b = 0
        a += 1
    continue
