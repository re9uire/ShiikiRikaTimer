# coding: utf-8
import ShiikiRikaModule as srm
import sys

if __name__ == "__main__":
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
            timer.Tloop()
        except Exception as e:
            print "+++ERROR!!+++"
            print "[ERROR_TYPE]:%s" % (str(type(e)))
            print "[ERROR_MESSAGE]:%s" % (str(e))
