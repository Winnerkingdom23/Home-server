import os.path
from os import path
import time
datum = time.localtime()
def openlogger():
    if os.path.exists("openinglogger.txt"):
        pass
    else:
        file = open("openinglogger.txt", "x")
        file.close()
    file = open("openinglogger.txt", "a")
    file.write(str(datum[0])+"."+str(datum[1])+"."+str(datum[2])+"\t"+str(datum[3])+":"+("0"+str(datum[4]))[-2:]+"\t"+str(datum[5])+" sec\n")
    file.close()
openlogger()





