# coding: utf-8
import time

i = int(raw_input("秒単位で入力してね:"))

while True:
    print "["+str(i)+"]:椎木里佳."
    i -= 1
    time.sleep(1)
    if i == 0:
        print "椎木里佳だマン"
        break
    continue
