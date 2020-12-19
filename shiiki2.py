# coding: utf-8
import random
import time

l = ["だよ","じゃん","では？","脆弱性対策して","CSSをパクるな","JK起業家","Go","株式会社AMF代表"]
i = int(raw_input("秒単位で入力してね:"))

while True:
    target = random.choice(l)
    print "["+str(i)+"]:椎木里佳"+target
    i -= 1
    time.sleep(1)
    if i == 0:
        print "椎木里佳だマン"
        break
    continue
