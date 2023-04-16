#Warren
import time
def reciprocal(starttime):
    nowtime = time.strftime('%H:%M:%S',time.localtime())#get current time
    if nowtime[0:2] != starttime[0:2]:
        nowtime = int(nowtime[3:5])*60+int(nowtime[6:8])+3600
    else:
        nowtime = int(nowtime[3:5])*60+int(nowtime[6:8])
    starttime = int(starttime[3:5])*60+int(starttime[6:8])#get the time in second
    if nowtime-starttime >= 150:
        return nowtime-starttime,True
    else:
        return nowtime-starttime,False#whether the time exceed 5 min
