from datetime import datetime
from time import clock
import time
from time import time, sleep
class Clock:
    hour = 0
    minute = 0
    second = 0
    formathour = 0
    formatmin = 0
    formatsec = 0
     
    def __init__(clock, h, m, s):
        clock.hour = h
        clock.minute = m
        clock.second = s
        #print(clock.hour)
        #print(clock.minute)
        #print(clock.second)

    def __str__(clock):
        clock.hour="{:02}".format(clock.hour)
        clock.minute="{:02}".format(clock.minute)
        clock.second="{:02}".format(clock.second)
        return f"{clock.hour}:{clock.minute}:{clock.second}"

    def tick(h,m,s,am='am'):
        myhr="{:02}".format(h)
        mymin="{:02}".format(m)
        mysec="{:02}".format(s)
        mys=int(mysec)
        mym=int(mymin)
        myh=int(myhr)
        print(f"{myhr}:{mymin}:{mysec} am")
        while True:
            mys=int(mys)
            mym=int(mym)
            myh=int(myh)
            try:
                    if int(mys)<59:
                        mys+=1
                        mys="{:02}".format(mys)
                        mym="{:02}".format(mym)
                        myh="{:02}".format(myh)
                        printtime=(f"{myh}:{mym}:{mys} am")
                    elif int(mym)==59 and int(mys)==59:
                        mys=0
                        mym=0
                        myh+=1
                        mys="{:02}".format(mys)
                        mym="{:02}".format(mym)
                        myh="{:02}".format(myh)
                        printtime=(f"{myh}:{mym}:{mys} am")
                    elif int(mys)==59:
                        mys=0
                        mym+=1
                        mys="{:02}".format(mys)
                        mym="{:02}".format(mym)
                        myh="{:02}".format(myh)
                        printtime=(f"{myh}:{mym}:{mys} am")
                    
                    
                    print(printtime)
                    sleep(1)

            except:
                    print("pass")
                    sleep(1)
                    pass
    
if __name__=="__main__": 
    h = int(input("What is the current hour ==> "))
    m = int(input("What is the current minute ==> "))
    s = int(input("What is the current second ==> "))
    num1 = Clock(h,m,s)
    Clock.tick(h,m,s, am='am')

    
