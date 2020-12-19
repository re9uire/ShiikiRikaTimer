# coding: utf-8
import time
import random

a = int(raw_input("Hour:"))
b = int(raw_input("Minute:"))
c = int(raw_input("Second:"))

one = ["name1","name2","name3"]
two = ["name4","name5","name6"]
three = ["name7","name8","name9"]
four = ["name10","name11","name12"]

while True:
    e = random.choice(one)
    f = random.choice(two)
    g = random.choice(three)
    h = random.choice(four)

    l = [e, f, g, h]

    p = random.choice(l)

    if p == e:
        print "[ %s : %s : %s : 1期 ]:%s." %(str(a),str(b),str(c),str(p))
    if p == f:
        print "[ %s : %s : %s : 2期 ]:%s." %(str(a),str(b),str(c),str(p))
    if p == g:
        print "[ %s : %s : %s : 3期 ]:%s." %(str(a),str(b),str(c),str(p))
    if p == h:
        print "[ %s : %s : %s : 4期 ]:%s." %(str(a),str(b),str(c),str(p))
    c -= 1
    time.sleep(1)
    if c < 0:
        c = 59
        b -= 1
    if b < 0:
        b = 59
        a -= 1
    if a < 0:
        print "JCJK調査隊(笑)"
        break
    continue
