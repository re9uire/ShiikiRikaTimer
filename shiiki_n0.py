# coding: utf-8
from datetime import datetime
import time
import sys

y = str(raw_input("Timer Name: "))
if y == "": y = "椎木里佳"
if y == "exit":
    print "See you..."
    sys.exit()
while True:
    print datetime.now().strftime("[ %Y / %m / %d | %H : %M : %S ]:" + str(y))
    time.sleep(1)
    continue
