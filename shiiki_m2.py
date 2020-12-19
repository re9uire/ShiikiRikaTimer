# coding: utf-8
import ShiikiRikaModule as srm
import sys

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
                if y == "exit":
                    print "See you..."
                    sys.exit()
                a = int(raw_input("Hour: "))
                b = int(raw_input("Minute: "))
                c = int(raw_input("Second: "))
                timer = srm.Timer(y, a, b, c)
                timer.TLoop()
            except Exception as e:
                print "+++ERROR!!+++"
                print "[ERROR_TYPE]:%s" % (str(type(e)))
                print "[ERROR_MESSAGE]:%s" % (str(e))
elif start == "2":
    try:
        y = str(raw_input("Stopper Name: "))
        if y == "exit":
             print "See you..."
             sys.exit()
        stopper = srm.Stopper(y)
        stopper.SLoop()
    except Exception as e:
        print "+++ERROR!!+++"
        print "[ERROR_TYPE]:%s" % (str(type(e)))
        print "[ERROR_MESSAGE]:%s" % (str(e))
elif start == "3":
    try:
        y = str(raw_input("Timer Name: "))
        if y == "exit":
             print "See you..."
             sys.exit()
        now = srm.Now(y)
        now.NLoop()
    except Exception as e:
        print "+++ERROR!!+++"
        print "[ERROR_TYPE]:%s" % (str(type(e)))
        print "[ERROR_MESSAGE]:%s" % (str(e))
elif start == "4":
    print "Exit"
    sys.exit()
else:
    print "nothing"
