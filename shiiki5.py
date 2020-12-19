# coding: utf-8
import time

a = int(raw_input("Hour:"))
b = int(raw_input("Minute:"))
c = int(raw_input("Second:"))
d = 0

while True:
    print "[ %s : %s : %s : %s ]:椎木里佳." %(str(a),str(b),str(c),str(d))
    d -= 1
    time.sleep(0.01)
    if d < 0:
        d = 99
        c -= 1
    if c < 0:
        c = 59
        b -= 1
    if b < 0:
        b = 59
        a -= 1
    if a < 0:
        print "椎木里佳だマン"
        break
    continue
