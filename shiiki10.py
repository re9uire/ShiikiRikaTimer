# coding: utf-8
import time
import sys
from datetime import datetime

print """
What do you use??
1, ShiikiRikaTimer
2, ShiikiRikaStopper
3, ShiikiRikaNow
4, Exit
    """
start = raw_input("Please enter 1-4: ")
if start == "1":
        while True:
            try:
                y = str(raw_input("Timer Name: "))
                if y == "": y = "椎木里佳"
                if y == "exit":
                    print "See you..."
                    sys.exit()
                a = int(raw_input("Hour: "))
                b = int(raw_input("Minute: "))
                c = int(raw_input("Second: "))
                while True:
                    print "[ %s : %s : %s ]:%s." %(str(a),str(b),str(c),str(y))
                    c -= 1
                    time.sleep(1)
                    if c < 0:
                        c = 59
                        b -= 1
                    if b < 0:
                        b = 59
                        a -= 1
                    if a < 0:
                        print "君の名は、%s" % str(y)
                        break
                    continue
            except Exception as e:
                print "+++ERROR!!+++"
                print "[ERROR_TYPE]:%s" % (str(type(e)))
                print "[ERROR_MESSAGE]:%s" % (str(e))
elif start == "2":
    try:
        y = str(raw_input("Stopper Name: "))
        if y == "": y = "椎木里佳"
        hour = 0
        minute = 0
        second = 0
        milli = 0
        while True:
            print "[ %s : %s : %s : %s ]:%s." %(str(hour),str(minute),str(second),str(milli),str(y))
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
    except Exception as e:
        print "+++ERROR!!+++"
        print "[ERROR_TYPE]:%s" % (str(type(e)))
        print "[ERROR_MESSAGE]:%s" % (str(e))
elif start == "3":
    try:
        y = str(raw_input("Timer Name: "))
        if y == "": y = "椎木里佳"
        if y == "exit":
            print "See you..."
            sys.exit()
        while True:
            print datetime.now().strftime("[ %Y / %m / %d | %H : %M : %S ]:" + str(y))
            time.sleep(1)
            continue
    except Exception as e:
        print "+++ERROR!!+++"
        print "[ERROR_TYPE]:%s" % (str(type(e)))
        print "[ERROR_MESSAGE]:%s" % (str(e))
elif start == "4":
    print "Exit"
    sys.exit()
else:
    print "nothing"
