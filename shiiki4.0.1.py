# coding: utf-8
import time

a = int(raw_input("Hour:"))
b = int(raw_input("Minute:"))
c = int(raw_input("Second:"))

while True:
    print "[ %s : %s : %s ]:椎木里佳." %(str(a),str(b),str(c))
    c -= 1
    time.sleep(1)
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
