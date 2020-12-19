# coding: utf-8
import time
import sys
import random
from datetime import datetime

class Timer(object):
     def __init__(self, name, hour, minute, second):
          self.name = name
          self.hour = hour
          self.minute = minute
          self.second = second
     def TLoop(self):
         if self.name == "": self.name = "椎木里佳"
         while True:
             print "[ %s : %s : %s ]:%s." %(self.hour, self.minute, self.second, self.name)
             self.second -= 1
             time.sleep(1)
             if self.second < 0:
                 self.second = 59
                 self.minute -= 1
             if self.minute < 0:
                 self.minute = 59
                 self.hour -= 1
             if self.hour < 0:
                 print "%sだマン" % self.name
                 break
             continue
class Stopper(object):
     def __init__(self, name):
          self.name = name
     def SLoop(self):
         hour = 0
         minute = 0
         second = 0
         milli = 0
         if self.name == "": self.name = "椎木里佳"
         while True:
             print "[ %s : %s : %s : %s ]:%s." %(str(hour),str(minute),str(second),str(milli),self.name)
             milli += 1
             time.sleep(0.01)
             if milli > 99:
                 milli = 0
                 second += 1
             if second > 59:
                 second = 0
                 minute += 1
             if minute > 59:
                 minute = 0
                 hour += 1
             continue
class Now(object):
     def __init__(self, name):
          self.name = name
     def NLoop(self):
         if self.name == "": self.name = "椎木里佳"
         while True:
             print datetime.now().strftime("[ %Y / %m / %d | %H : %M : %S ]:" + self.name)
             time.sleep(1)
             continue
if __name__ == "__main__":
    y = str(raw_input("Timer Name: "))
    a = int(raw_input("Hour: "))
    b = int(raw_input("Minute: "))
    c = int(raw_input("Second: "))
    timer = Timer(y, a, b, c)
    timer.mainloop()
